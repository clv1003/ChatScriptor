from transformers import pipeline
import os.path


class Traductor:
    def traductor(self, text):
        pass


class TraductorAdaptador(Traductor):
    def __init__(self, model_names):
        self.translators = {}
        for source_lang, target_lang, model_name in model_names:
            self.translators[(source_lang, target_lang)] = pipeline("translation", model=model_name,
                                                                    src_lang=source_lang, tgt_lang=target_lang)

    def traducir(self, text, source_language, target_language):
        key = (source_language, target_language)
        if key in self.translators:
            result = self.translators[key](text)
            return result[0]['translation_text']
        else:
            raise ValueError(
                f"No se encontró un modelo de traducción para el par de idiomas: {source_language}-{target_language}")


def traducirArchivo(rootdir, chat, original1, original2, archivo1, archivo2, tipo):
    if original1.endswith('.json') and original2.endswith('.json') and archivo1.endswith('.json') and archivo2.endswith(
            '.json'):

        if tipo == 'entidad':
            rutaOr1 = rootdir + chat + '/entities/' + original1
            os.rename(rutaOr1, archivo1)

        elif tipo == 'intent':
            rutaOr1 = rootdir + chat + '/intents/' + original1
            os.rename(rutaOr1, archivo1)

