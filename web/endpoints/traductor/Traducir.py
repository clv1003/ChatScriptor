from traductor import TraducirAgente, TraducirEntidades, TraducirIntents
from traductor.Traductor import Traductor

import os.path
import ProcesamientoAgente
import ProcesamientoArchivos
import time

'''
def traducir(rootdir, chatbot, idioma):
    modelos = [
        # Inglés
        ("en", "es", "Helsinki-NLP/opus-mt-en-es"),  # a Español
        #("en", "fr", "Helsinki-NLP/opus-mt-en-fr"),  # a Francés
        #("en", "de", "Helsinki-NLP/opus-mt-en-de"),  # a Alemán
        # Español
        ("es", "en", "Helsinki-NLP/opus-mt-es-en")  # a Inglés
        #("es", "fr", "Helsinki-NLP/opus-mt-es-fr"),  # a Francés
        #("es", "de", "Helsinki-NLP/opus-mt-es-de"),  # a Alemán
        # Francés
        #("fr", "es", "Helsinki-NLP/opus-mt-fr-es"),  # a Español
        #("fr", "en", "Helsinki-NLP/opus-mt-fr-en"),  # a Inglés
        #("fr", "de", "Helsinki-NLP/opus-mt-fr-de"),  # a Alemán
        # Alemán
        #("de", "es", "Helsinki-NLP/opus-mt-de-es"),  # a Español
        #("de", "en", "Helsinki-NLP/opus-mt-de-en"),  # a Inglés
        #("de", "fr", "Helsinki-NLP/opus-mt-de-de"),  # a Francés
    ]

    traductor = Traductor.TraductorAdaptador(modelos)
    original = ProcesamientoAgente.get_agente_language(rootdir + chatbot)
    print(f'')
    print(f"\033[91m ---------------------------- TRADUCTOR de {original} a {idioma}\033[0m")

    # Nombre nuevo chatbot
    chat = traductor.traducir(chatbot, original, idioma)
    ProcesamientoArchivos.copiarDir(rootdir, chatbot, chat)

    if os.path.exists(rootdir + chat):
        TraducirAgente.traducirAgente(traductor, rootdir, chat, original, idioma)
        TraducirEntidades.traducirEntidades(traductor, rootdir, chat, original, idioma)
        TraducirIntents.traducirIntents(traductor, rootdir, chat, original, idioma)

        return chat
'''


def traducir(rootdir, chatbot, idioma):
    inicio = time.time()
    original = ProcesamientoAgente.get_agente_language(rootdir + chatbot)
    print(f'')
    print(f"\033[35mTRADUCTOR de {original} a {idioma}\033[0m")

    traductor = Traductor(original, idioma)

    chat = traductor.traducirFrase(chatbot)
    ProcesamientoArchivos.copiarDir(rootdir, chatbot, chat)
    print(f'Nuevo nombre ({chatbot}): {chat} ')

    if os.path.exists(rootdir + chat):

        TraducirAgente.traducirAgente(traductor, rootdir, chat)
        TraducirEntidades.traducirEntidades(traductor, rootdir, chat)
        TraducirIntents.traducirIntents(traductor, rootdir, chat)
        print(f'\033[34mTiempo: {time.time() - inicio} \033[0m')
        return chat
