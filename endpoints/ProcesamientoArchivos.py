import os, re


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


def relistado(cadena):
    valores = re.findall(r"'(.*?)'", cadena)
    return [valores[0], valores[1]]


