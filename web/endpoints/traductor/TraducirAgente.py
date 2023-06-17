
import os.path

from unidecode import unidecode

import ProcesamientoAgente

'''
def traducirAgente(traductor, rootdir, chat, original, idioma):
    if os.path.exists(rootdir + chat):
        agente = ProcesamientoAgente.get_agente(rootdir + chat)

        print(f'')
        print("\033[91m ---------------------------- AGENTE \033[0m")
        
        displayName = agente['displayName']
        shortDescription = agente['shortDescription']
        description = agente['description']
        examples = agente['examples']

        tr_displayName = traductor.traducir(displayName, original, idioma)
        tr_shortDescription = traductor.traducir(shortDescription, original, idioma)
        tr_description = traductor.traducir(description, original, idioma)
        tr_examples = traductor.traducir(examples, original, idioma)

        print(f'{displayName} - {tr_displayName}')
        print(f'{shortDescription} - {tr_shortDescription}')
        print(f'{description} - {tr_description}')
        print(f'{examples} - {tr_examples}')

        cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples, idioma)


def cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples, tr_idioma):
    ProcesamientoAgente.set_agente(rootdir, chat, 'displayName', unidecode(tr_displayName))
    ProcesamientoAgente.set_agente(rootdir, chat, 'shortDescription', tr_shortDescription)
    ProcesamientoAgente.set_agente(rootdir, chat, 'description', tr_description)
    ProcesamientoAgente.set_agente(rootdir, chat, 'examples', tr_examples)
    ProcesamientoAgente.set_agente(rootdir, chat, 'language', tr_idioma)
'''


def traducirAgente(traductor, rootdir, chat):
    if os.path.exists(rootdir + chat):
        agente = ProcesamientoAgente.get_agente(rootdir + chat)

        print(f'')
        print("\033[91m ---------------------------- AGENTE \033[0m")

        diccionario = {
            'displayName': agente['displayName'],
            'shortDescription': agente['shortDescription'],
            'description': agente['description'],
            'examples': agente['examples']
        }

        tr_diccionario = traductor.traducirDiccionario(diccionario)

        ProcesamientoAgente.set_agente(rootdir, chat, 'displayName', unidecode(tr_diccionario['displayName']))
        print("\033[92m -> OK! - Modificado displayName \033[0m")
        ProcesamientoAgente.set_agente(rootdir, chat, 'shortDescription', tr_diccionario['shortDescription'])
        print("\033[92m -> OK! - Modificado shortDescription \033[0m")
        ProcesamientoAgente.set_agente(rootdir, chat, 'description', tr_diccionario['description'])
        print("\033[92m -> OK! - Modificado description \033[0m")
        ProcesamientoAgente.set_agente(rootdir, chat, 'examples', tr_diccionario['examples'])
        print("\033[92m -> OK! - Modificado examples2 \033[0m")
        ProcesamientoAgente.set_agente(rootdir, chat, 'language', traductor.getIdioma())
        print("\033[92m -> OK! - Modificado idioma \033[0m")
