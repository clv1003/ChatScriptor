import os.path

from unidecode import unidecode

import ProcesamientoEntidadesIntents

'''
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

            if 'speech' in datos[0]['responses'][0]['messages'][0]:
                speech = datos[0]['responses'][0]['messages'][0]['speech']

                for s in speech:
                    tr_speech = traductor.traducir(s, original, idioma)
                    print(f'{tr_speech}')
                    ProcesamientoEntidadesIntents.editar_messages(dirs[0], s, tr_speech)
                print("\033[92m -> OK! - Modificado Speech \033[0m")

            for i in datos[1]:
                for j in i['data']:
                    if len(j) == 2:
                        text = j['text']
                        if len(text) > 0:
                            tr_text = traductor.traducir(text, original, idioma)
                            print(f'{tr_text}')
                            ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text
                                                                      , original)
                            print("\033[92m -> OK! - Modificado text 1 \033[0m")
                    elif j['meta']:
                        text = j['text']
                        if len(text) > 0:
                            tr_text = traductor.traducir(text, original, idioma)

                            print(f'{tr_text}')
                            ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text
                                                                      , original)
                            print("\033[92m -> OK! - Modificado text 2 \033[0m")

            if intent[1].endswith('_usersays_' + original + '.json'):
                nombreNuevo = intent[0].replace('.json', '') + '_usersays_' + idioma + '.json'
                rutaNueva = rootdir + chat + '/intents/' + nombreNuevo
                print(f'Cambio de directorio: {nombreNuevo} --> {rutaNueva}')
                print(f'')
                os.rename(dirs[1], rutaNueva)
'''


def traducirIntents(traductor, rootdir, chat):
    if os.path.exists(rootdir + chat + '/intents'):
        print(f'')
        print("\033[91m---------------------------- INTENTS \033[0m")
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat, traductor.getOriginal())

        for intent in intents:
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent[0], traductor.getOriginal())
            datos = ProcesamientoEntidadesIntents.get_json(dirs[0], dirs[1])

            if 'speech' in datos[0]['responses'][0]['messages'][0]:
                speech = datos[0]['responses'][0]['messages'][0]['speech']

                for s in speech:
                    tr_speech = traductor.traducirFrase(s)
                    ProcesamientoEntidadesIntents.editar_messages(dirs[0], s, tr_speech)

            for i in datos[1]:
                for j in i['data']:
                    if len(j) == 2:
                        text = j['text']
                        if len(text) > 0:
                            tr_text = traductor.traducirFrase(text)
                            ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text
                                                                      , traductor.getOriginal())
                    elif j['meta']:
                        text = j['text']
                        if len(text) > 0:
                            tr_text = traductor.traducirFrase(text)
                            ProcesamientoEntidadesIntents.editar_data(rootdir+chat, intent[0], text, 'text', tr_text
                                                                      , traductor.getOriginal())
            print(f"\033[92m-> OK! - Traducido intent {intent[0]}\033[0m")

            if intent[1].endswith('_usersays_' + traductor.getOriginal() + '.json'):
                nombreNuevo = intent[0].replace('.json', '') + '_usersays_' + traductor.getIdioma() + '.json'
                rutaNueva = rootdir + chat + '/intents/' + nombreNuevo
                print(f' -> Directorio: {nombreNuevo} --> {rutaNueva}')
                os.rename(dirs[1], rutaNueva)