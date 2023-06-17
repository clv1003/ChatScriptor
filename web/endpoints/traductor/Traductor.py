from transformers import pipeline, MarianMTModel, MarianTokenizer
import os.path

'''
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

'''


class Traductor:
    def __init__(self, original, idioma):
        modelos = {
            'en-es': {
                'model_name': 'Helsinki-NLP/opus-mt-en-es',
                'tokenizer_name': 'Helsinki-NLP/opus-mt-en-es'
            },
            'es-en': {
                'model_name': 'Helsinki-NLP/opus-mt-es-en',
                'tokenizer_name': 'Helsinki-NLP/opus-mt-es-en'
            }
        }

        model_name = modelos[f'{original}-{idioma}']['model_name']
        tokenizer_name = modelos[f'{original}-{idioma}']['tokenizer_name']

        self.modelo = MarianMTModel.from_pretrained(model_name)
        self.token = MarianTokenizer.from_pretrained(tokenizer_name)

        self.original = original
        self.idioma = idioma

    def getOriginal(self):
        return self.original

    def getIdioma(self):
        return self.idioma

    def traducirFrase(self, frase, max_length=512):
        input = self.token(frase, return_tensors='pt')
        input_ids = input['input_ids']
        attention_mask = input['attention_mask']

        tr_model = self.modelo.generate(input_ids=input_ids,
                                        attention_mask=attention_mask,
                                        max_length=max_length)
        tr_token = self.token.decode(tr_model[0], skip_special_tokens=True)

        return tr_token

    def traducirDiccionario(self, diccionario):
        tr_diccionario = {}

        for clave, frase in diccionario.items():
            tr_frase = self.traducirFrase(frase)
            tr_diccionario[clave] = tr_frase

        return tr_diccionario

