import os.path
import ProcesamientoEntidadesIntents

'''
def traducirEntidades(traductor, rootdir, chat, original, idioma):
    if os.path.exists(rootdir + chat + '/entities'):
        print(f'')
        print("\033[91m ---------------------------- ENTIDADES \033[0m")
        print(f'{rootdir + chat}')
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat, original)
        print(f'{entidades}')
        print(f'')

        for entidad in entidades:
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad[0], original)
            datos = ProcesamientoEntidadesIntents.get_json(dirs[0], dirs[1])

            for e in datos[1]:
                value = e["value"]
                synonyms = eval(str(e["synonyms"]))
                print(f'{synonyms}')
                tr_value = traductor.traducir(value, original, idioma)
                tr_synonyms = traductor.traducir(synonyms, original, idioma)
                print(f'{tr_value} - {tr_synonyms}')
                ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0], tr_value, original)
                ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0], tr_synonyms, original)
                print("\033[92m -> OK! - Modificado value y sinonimos \033[0m")
            if entidad[1].endswith('_entries_' + original + '.json'):
                nombreNuevo = entidad[0].replace('.json', '') + '_entries_' + idioma + '.json'
                rutaNueva = rootdir + chat + '/entities/' + nombreNuevo
                print(f'Cambio de directorio: {nombreNuevo} --> {rutaNueva}')
                print(f'')
                os.rename(dirs[1], rutaNueva)
'''


def traducirEntidades(traductor, rootdir, chat):
    if os.path.exists(rootdir + chat + '/entities'):
        print(f'')
        print("\033[91m---------------------------- ENTIDADES \033[0m")
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat, traductor.getOriginal())

        for entidad in entidades:
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad[0],
                                                                    traductor.getOriginal())
            datos = ProcesamientoEntidadesIntents.get_json(dirs[0], dirs[1])
            for e in datos[1]:
                value = e["value"]
                synonyms = e["synonyms"]
                diccionarioSynonyms = {synonym: synonym for synonym in synonyms}

                tr_value = traductor.traducirFrase(value)
                tr_synonyms = traductor.traducirDiccionario(diccionarioSynonyms)
                tr_synonyms = list(tr_synonyms.values())

                ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0], tr_value,
                                                           traductor.getOriginal())
                ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, tr_value, entidad[0], tr_synonyms,
                                                           traductor.getOriginal())

            print(f"\033[92m-> OK! - Traducido entidad {entidad[0]}\033[0m")

            if entidad[1].endswith('_entries_' + traductor.getOriginal() + '.json'):
                nombreNuevo = entidad[0].replace('.json', '') + '_entries_' + traductor.getIdioma() + '.json'
                rutaNueva = rootdir + chat + '/entities/' + nombreNuevo
                print(f' -> Directorio: {nombreNuevo} --> {rutaNueva}')
                os.rename(dirs[1], rutaNueva)
