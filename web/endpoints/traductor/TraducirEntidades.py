import os.path
import ProcesamientoEntidadesIntents


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

            name = datos[0]["name"]
            tr_name = traductor.traducir(name, original, idioma)
            print(f'{tr_name}')
            ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name)
            print("\033[92m -> OK! - Modificado nombre \033[0m")
            for e in datos[1]:
                value = e["value"]
                synonyms = e["synonyms"]

                tr_value = traductor.traducir(value, original, idioma)
                tr_synonyms = traductor.traducir(synonyms, original, idioma)
                print(f'{tr_value} - {tr_synonyms}')
                ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0], tr_value, original)
                ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0], tr_synonyms, original)
                print("\033[92m -> OK! - Modificado value y sinonimos \033[0m")
            if entidad[1].endswith('_entries_' + original + '.json'):
                nombreNuevo = entidad[0].replace('.json', '') + '_entries_' + idioma + '.json'
                rutaNueva = rootdir + chat + '/entities/' + nombreNuevo
                print(f'{nombreNuevo} --> {rutaNueva}')
                print(f'')
                os.rename(dirs[1], rutaNueva)
