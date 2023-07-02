# IMPORTS
import os.path
from web.endpoints.ProcesamientoEntidadesIntents import *

'''
TRADUCIR ENTIDADES
@Author: Claudia Landeira

Funciones encargadas de realizar la traduccion del bloque de entidades
'''


# FUNCION --> traducirEntidades
# Función encargada de traducir los datos de las entidades
def traducirEntidades(traductor, rootdir, chat):
    if os.path.exists(rootdir + chat + '/entities'):
        print(f'')
        print("\033[91m---------------------------- ENTIDADES \033[0m")
        entidades = getEntidades(rootdir + chat, traductor.getOriginal())

        for entidad in entidades:
            dirs = directoriosEntidad(rootdir + chat, entidad[0],
                                                                    traductor.getOriginal())
            datos = get_json(dirs[0], dirs[1])

            name = datos[0]['name']
            tr_name = traductor.traducirFrase(name)

            for e in datos[1]:
                value = e["value"]
                synonyms = e["synonyms"]
                diccionarioSynonyms = {synonym: synonym for synonym in synonyms}

                tr_value = traductor.traducirFrase(value)
                tr_synonyms = traductor.traducirDiccionario(diccionarioSynonyms)
                tr_synonyms = list(tr_synonyms.values())

                editar_v_ent(rootdir + chat, value, entidad[0], tr_value, traductor.getOriginal())
                editar_s_ent(rootdir + chat, tr_value, entidad[0], tr_synonyms, traductor.getOriginal())

            editar_nombre(dirs[0], 'name', tr_name)

            print(f"\033[92m-> OK! - Traducido entidad {entidad[0]}\033[0m")

            if entidad[1].endswith('_entries_' + traductor.getOriginal() + '.json'):
                nombreNuevo = entidad[0].replace('.json', '') + '_entries_' + traductor.getIdioma() + '.json'
                rutaNueva = rootdir + chat + '/entities/' + nombreNuevo
                print(f' -> Directorio: {nombreNuevo} --> {rutaNueva}')
                os.rename(dirs[1], rutaNueva)
