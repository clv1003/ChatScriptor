import os
import platform
import shutil
import zipfile
from flask import request


# DESCOMPRIMIR EL ARCHIVO IMPORTADO
def descomprimir_archivo(rootdir):
    f = request.files['archivo_zip']

    if f.filename.endswith('.zip'):
        fnombre = f.filename
        f.save(fnombre)

        with zipfile.ZipFile(fnombre, 'r') as zip_ref:
            zip_ref.extractall(rootdir + '/' + os.path.splitext(f.filename)[0])
        os.remove(fnombre)


# EXPORTAR EL ARCHIVO INDICADO
def exportar_archivos(rootdir, name):  # rootdir = ./unzip/ ; name = Weather
    if os.path.exists(rootdir + name):
        downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

        if os.path.exists(downloads_dir + '/' + name + '.zip'):
            num = 1
            while os.path.exists(downloads_dir + '/' + name + '(' + str(num) + ')' + '.zip'):
                num += 1

            fnombre = name + '(' + str(num) + ')'
            zip_dir = shutil.make_archive(fnombre, format='zip', root_dir=rootdir + name)

            shutil.move(zip_dir, downloads_dir)
            print(f'\033[34mEl chatbot se ha descargado\033[0m')

        else:
            zip_dir = shutil.make_archive(name, format='zip', root_dir=rootdir + name)
            shutil.move(zip_dir, downloads_dir)
            print(f'\033[34mEl chatbot se ha descargado\033[0m')


# ELIMINAR EL CONTENIDO DEL DIRECTORIO UNZIP
def remove_unzip():
    shutil.rmtree('./unzip')
