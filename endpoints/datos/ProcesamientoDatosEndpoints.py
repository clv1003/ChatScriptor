import json
import os
import shutil
import zipfile

from flask import request


def descomprimir_archivo():
    f = request.files['archivo_zip']

    if f.filename.endswith('.zip'):
        fnombre = f.filename
        f.save(fnombre)

        with zipfile.ZipFile(fnombre, 'r') as zip_ref:
            zip_ref.extractall('unzip/' + os.path.splitext(f.filename)[0])
        os.remove(fnombre)


def get_disponible(rootdir):
    if os.path.exists(rootdir):
        return os.listdir(rootdir)


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


def get_agente(rootdir):
    if os.path.exists(rootdir + '/agent.json'):
        with open(rootdir + '/agent.json', 'r') as a:
            agente = json.load(a)

            return agente

    else:
        return None


def get_entidades(rootdir):
    return rootdir
    pass


def get_entidad():
    pass


def get_intents(rootdir):
    return rootdir
    pass


def get_intent():
    pass


def remove_unzip():
    directorio_temporal = './unzip'
    shutil.rmtree(directorio_temporal)
    os.mkdir(directorio_temporal)
