import os
import shutil
import zipfile
from flask import request


# DESCOMPRIMIR EL ARCHIVO IMPORTADO
def descomprimir_archivo(rootdir):
    f = request.files['archivo_zip']

    if f.filename.endswith('.zip'):
        fnombre = f.filename
        f.save(fnombre)

        if comprobar_estructura(f.filename):
            with zipfile.ZipFile(fnombre, 'r') as zip_ref:
                zip_ref.extractall(rootdir + '/' + os.path.splitext(f.filename)[0])
            os.remove(fnombre)
            return True

        os.remove(fnombre)
        return False
    return False


# EXPORTAR EL ARCHIVO INDICADO
def exportar_archivos(rootdir, name):
    if os.path.exists(rootdir + name):
        zip_dir = shutil.make_archive(name, format='zip', root_dir=rootdir + name)
        print(f'\033[34mEl chatbot se ha descargado\033[0m')
        return zip_dir


def comprobar_estructura(archivo_zip):
    estructura = ['entities', 'intents', 'agent.json', 'package.json']

    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        estructura_zip = set()

        for nombre in zip_ref.namelist():
            pr_estructura_zip = os.path.split(nombre)[0]
            if pr_estructura_zip:
                estructura_zip.add(pr_estructura_zip)

        for nombre in zip_ref.namelist():
            if '/' not in nombre:
                estructura_zip.add(nombre)

        if estructura_zip == set(estructura):
            return True
        else:
            return False
