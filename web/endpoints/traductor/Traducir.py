from traductor import TraducirAgente, TraducirEntidades, TraducirIntents
from traductor.Traductor import Traductor

import os.path
import ProcesamientoAgente
import ProcesamientoArchivos
import time


def traducir(rootdir, chatbot, idioma):
    inicio = time.time()
    original = ProcesamientoAgente.get_agente_language(rootdir + chatbot)
    print(f'')
    print(f"\033[35mTRADUCTOR de {original} a {idioma}\033[0m")

    traductor = Traductor(original, idioma)

    chat = traductor.traducirFrase(chatbot)
    if chat == chatbot:
        chat = chat + f' ({idioma})'
        ProcesamientoArchivos.copiarDir(rootdir, chatbot, chat)
    else:
        ProcesamientoArchivos.copiarDir(rootdir, chatbot, chat)

    print(f'Nuevo nombre ({chatbot}): {chat} ')

    if os.path.exists(rootdir + chat):

        TraducirAgente.traducirAgente(traductor, rootdir, chat)
        TraducirEntidades.traducirEntidades(traductor, rootdir, chat)
        TraducirIntents.traducirIntents(traductor, rootdir, chat)
        print(f'\033[34mTiempo: {time.time() - inicio} \033[0m')
        return chat
