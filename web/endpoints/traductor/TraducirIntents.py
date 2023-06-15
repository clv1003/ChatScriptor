import os.path
import ProcesamientoEntidadesIntents


def traducirIntents(traductor, rootdir, chat, original, idioma):
    if os.path.exists(rootdir + chat + '/intents'):
        print(f'')
        print("\033[91m ---------------------------- INTENTS \033[0m")
        print(f'{rootdir + chat}')
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat, original)
        print(f'{intents}')
        print(f'')

        for intent in intents:
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent[0], original)
            datos = ProcesamientoEntidadesIntents.get_json(dirs[0], dirs[1])
            name = datos[0]['name']
            action = datos[0]['responses'][0]['action']

            tr_name = traductor.traducir(name, original, idioma)
            tr_action = traductor.traducir(action, original, idioma)
            print(f'{tr_name} - {tr_action}')
            ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name)
            ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action)
            print("\033[92m -> OK! - Modificado nombre y action \033[0m")

            if datos[0]['responses'][0]['parameters']:
                for i in datos[0]['responses'][0]['parameters']:
                    nombre = i['name']
                    dataType = i['dataType']
                    value = i['value']

                    tr_nombre = traductor.traducir(nombre, original, idioma)
                    tr_dataType = traductor.traducir(dataType, original, idioma)
                    tr_value = traductor.traducir(value, original, idioma)
                    print(f'{tr_nombre} - {tr_dataType} - {tr_value}')
                    ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre)
                    ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType', tr_dataType)
                    ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value)
                    print("\033[92m -> OK! - Modificado nombre, datatype y value \033[0m")

            if 'speech' in datos[0]['responses'][0]['messages'][0]:
                speech = datos[0]['responses'][0]['messages'][0]['speech']
                traducido = []

                for s in speech:
                    tr_speech = traductor.traducir(s, original, idioma)
                    traducido.append(tr_speech)
                print(f'{traducido}')
                ProcesamientoEntidadesIntents.editar_messages(dirs[0], speech, traducido)
                print("\033[92m -> OK! - Modificado Speech \033[0m")

            for i in datos[1]:
                for j in i['data']:
                    if len(j) == 2:
                        text = j['text']
                        tr_text = traductor.traducir(text, original, idioma)
                        print(f'{tr_text}')
                        ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text, original)
                        print("\033[92m -> OK! - Modificado text \033[0m")
                    elif j['meta']:
                        text = j['text']
                        meta = j['meta']
                        alias = j['alias']

                        tr_text = traductor.traducir(text, original, idioma)
                        tr_meta = traductor.traducir(meta, original, idioma)
                        tr_alias = traductor.traducir(alias, original, idioma)
                        print(f'{tr_text} - {tr_meta} - {tr_alias}')
                        ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text
                                                                  , original)
                        ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], meta, 'meta', tr_meta
                                                                  , original)
                        ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], alias, 'alias', tr_alias
                                                                  , original)
                        print("\033[92m -> OK! - Modificado text, meta y alias \033[0m")

            if intent[1].endswith('_usersays_' + original + '.json'):
                nombreNuevo = intent[0].replace('.json', '') + '_usersays_' + idioma + '.json'
                rutaNueva = rootdir + chat + '/intents/' + nombreNuevo
                print(f'{nombreNuevo} --> {rutaNueva}')
                print(f'')
                os.rename(dirs[1], rutaNueva)
