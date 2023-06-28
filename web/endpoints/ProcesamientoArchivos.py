import os
import re
import shutil

from web.endpoints.ProcesamientoAgente import getAgente
from web.endpoints.ProcesamientoEntidadesIntents import getEntidades, getIntents


def get_disponible(rootdir):
    chatbots = []

    if os.path.exists(rootdir):
        for file in os.listdir(rootdir):
            if file != 'readme.md':
                chatbots.append(file)

    return chatbots


def get_arbol(rootdir):
    arbol = {}

    for subdir, dirs, files in os.walk(rootdir):
        subdir_rel = os.path.relpath(subdir, rootdir)
        aux_arbol = arbol

        if subdir_rel != '.':
            for d in subdir_rel.split(os.sep):
                aux_arbol = aux_arbol.setdefault(d, {})

        for file in files:
            aux_arbol[file] = None

    return arbol


def relistado(cadena):
    valores = re.findall(r"'(.*?)'", cadena)
    return [valores[0], valores[1]]


def removeChatbot(rootdir, chat):
    shutil.rmtree(rootdir + chat)


def obtener_datos(rootdir, chatbots):
    diccionarioAgentes = {}
    diccionarioEntidades = {}
    diccionarioIntents = {}

    for c in chatbots:
        diccionarioAgentes[c] = getAgente(rootdir + '/' + c)
        diccionarioEntidades[c] = getEntidades(rootdir + '/' + c)
        diccionarioIntents[c] = getIntents(rootdir + '/' + c)

    return diccionarioAgentes, diccionarioEntidades, diccionarioIntents


def copiarDir(rootdir, chat, nombre):
    try:
        shutil.copytree(rootdir + chat, './' + nombre)
        shutil.move('./' + nombre, rootdir)
    except shutil.Error as e:
        print(f'Error al copiar directorio: {e}')
    except OSError as e:
        print(f'Error de sistema al copiar el directorio: {e}')
