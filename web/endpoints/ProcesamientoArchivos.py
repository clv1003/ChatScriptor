import os
import re
import shutil


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


def remove_chatbot(rootdir, chat):
    shutil.rmtree(rootdir+chat)
