import os.path

import ProcesamientoAgente

from traductor import es
from traductor import de
from traductor import en
from traductor import fr


def traducir(rootdir, idioma, chat):
    original = ProcesamientoAgente.get_agente_language(rootdir + chat)

    if original == 'en':
        if idioma == 'es':
            return en.tr_en_es(chat, rootdir, original, idioma)

        if idioma == 'fr':
            return en.tr_en_fr(chat, rootdir, original, idioma)

        if idioma == 'de':
            return en.tr_en_de(chat, rootdir, original, idioma)

    if original == 'es':
        if idioma == 'en':
            return es.tr_es_en(chat, rootdir, original, idioma)

        if idioma == 'fr':
            return es.tr_es_fr(chat, rootdir, original, idioma)

        if idioma == 'de':
            return es.tr_es_de(chat, rootdir, original, idioma)

    if original == 'fr':
        if idioma == 'en':
            return fr.fr_en(chat, rootdir, original, idioma)

        if idioma == 'es':
            return fr.fr_es(chat, rootdir, original, idioma)

        if idioma == 'de':
            return fr.fr_de(chat, rootdir, original, idioma)

    if original == 'de':
        if idioma == 'en':
            return de.de_en(chat, rootdir, original, idioma)

        if idioma == 'es':
            return de.de_es(chat, rootdir, original, idioma)

        if idioma == 'fr':
            return de.de_fr(chat, rootdir, original, idioma)


def cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples, tr_idioma):
    ProcesamientoAgente.set_agente(rootdir, chat, 'displayName', tr_displayName[0]['translation_text'])
    ProcesamientoAgente.set_agente(rootdir, chat, 'language', tr_idioma)
    ProcesamientoAgente.set_agente(rootdir, chat, 'shortDescription', tr_shortDescription[0]['translation_text'])
    ProcesamientoAgente.set_agente(rootdir, chat, 'description', tr_description[0]['translation_text'])
    ProcesamientoAgente.set_agente(rootdir, chat, 'examples', tr_examples[0]['translation_text'])


def traducirArchivo(rootdir, chat, original1, original2, archivo1, archivo2, tipo):
    if original1.endswith('.json') and original2.endswith('.json') and archivo1.endswith('.json') and archivo2.endswith(
            '.json'):

        if tipo == 'entidad':
            rutaOr1 = rootdir + chat + '/entities/' + original1
            rutaOr2 = rootdir + chat + '/entities/' + original2
            os.rename(rutaOr1, archivo1)
            os.rename(rutaOr2, archivo2)

        elif tipo == 'intent':
            rutaOr1 = rootdir + chat + '/intents/' + original1
            rutaOr2 = rootdir + chat + '/intents/' + original2
            os.rename(rutaOr1, archivo1)
            os.rename(rutaOr2, archivo2)


