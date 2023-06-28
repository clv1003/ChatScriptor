from web.endpoints.traductor.TraducirAgente import *
from web.endpoints.traductor.TraducirEntidades import *
from web.endpoints.traductor.TraducirIntents import *
from web.endpoints.traductor.Traductor import Traductor
from web.endpoints.ProcesamientoAgente import *
from web.endpoints.ProcesamientoArchivos import *
import os.path
import time


def traducir(rootdir, chatbot, idioma):
    inicio = time.time()
    original = get_agente_language(rootdir + chatbot)
    print(f'')
    print(f"\033[35mTRADUCTOR de {original} a {idioma}\033[0m")

    traductor = Traductor(original, idioma)

    chat = traductor.traducirFrase(chatbot)
    if chat == chatbot:
        chat = chat + f' ({idioma})'
        copiarDir(rootdir, chatbot, chat)
    else:
        copiarDir(rootdir, chatbot, chat)

    print(f'Nuevo nombre ({chatbot}): {chat} ')

    if os.path.exists(rootdir + chat):

        traducirAgente(traductor, rootdir, chat)
        traducirEntidades(traductor, rootdir, chat)
        traducirIntents(traductor, rootdir, chat)
        print(f'\033[34mTiempo: {time.time() - inicio} \033[0m')
        return chat
