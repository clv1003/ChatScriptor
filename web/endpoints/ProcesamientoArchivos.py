# IMPORTS
import os
import re
import shutil

from web.endpoints.ProcesamientoAgente import getAgente
from web.endpoints.ProcesamientoEntidadesIntents import getEntidades, getIntents

'''
PROCESAMIENTO ARCHIVOS
@Author: Claudia Landeira

Funciones encargadas de realizar acciones generales sobre los archivos de los chatbots
'''


# FUNCION --> get_disponible
# Función encargada de obtener todos los chatbos disponibles de un usuario
def get_disponible(rootdir):
    chatbots = []

    if os.path.exists(rootdir):
        for file in os.listdir(rootdir):
            if file != 'readme.md':
                chatbots.append(file)

    return chatbots


# FUNCION --> get_arbol
# Función encargada de obtener el arbol de archivos que contiene un chatbot
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


# FUNCION --> relistado
# Función encargada de convertir valores entre comillas en una cadena
def relistado(cadena):
    valores = re.findall(r"'(.*?)'", cadena)
    return [valores[0], valores[1]]


# FUNCION --> removeChatbot
# Función encargada de eliminar un chatbot del sistema
def removeChatbot(rootdir, chat):
    shutil.rmtree(rootdir + chat)


# FUNCION --> obtener_datos
# Función encargada de recoger los datos de todos los chatbots de un usuario
def obtener_datos(rootdir, chatbots):
    diccionarioAgentes = {}
    diccionarioEntidades = {}
    diccionarioIntents = {}

    for c in chatbots:
        diccionarioAgentes[c] = getAgente(rootdir + '/' + c)
        diccionarioEntidades[c] = getEntidades(rootdir + '/' + c)
        diccionarioIntents[c] = getIntents(rootdir + '/' + c)

    return diccionarioAgentes, diccionarioEntidades, diccionarioIntents


# FUNCION --> copiarDir
# Función encargada de copiar el chatbot completo de un usuario
def copiarDir(rootdir, chat, nombre):
    try:
        shutil.copytree(rootdir + chat, './' + nombre)
        shutil.move('./' + nombre, rootdir)
    except shutil.Error as e:
        print(f'Error al copiar directorio: {e}')
    except OSError as e:
        print(f'Error de sistema al copiar el directorio: {e}')
