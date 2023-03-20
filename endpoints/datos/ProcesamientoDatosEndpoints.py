import json
import os
import zipfile

from flask import request


def descomprimir_archivo():
    f = request.files['archivo_zip']
    fnombre = f.filename
    f.save(fnombre)

    with zipfile.ZipFile(fnombre, 'r') as zip_ref:
        zip_ref.extractall('unzip')
    os.remove(fnombre)


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
        with open(rootdir+'/agent.json', 'r') as agente:
            return json.load(agente)


def get_entidades(rootdir):
    pass


def get_entidad():
    pass


def get_intents(rootdir):
    pass


def get_intent():
    pass
