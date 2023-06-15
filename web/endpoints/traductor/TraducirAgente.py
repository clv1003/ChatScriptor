
import os.path
import ProcesamientoAgente


def traducirAgente(traductor, rootdir, chat, original, idioma):
    if os.path.exists(rootdir + chat):
        agente = ProcesamientoAgente.get_agente(rootdir + chat)

        displayName = agente['displayName']
        shortDescription = agente['shortDescription']
        description = agente['description']
        examples = agente['examples']

        tr_displayName = traductor.traducir(displayName, original, idioma)
        tr_shortDescription = traductor.traducir(shortDescription, original, idioma)
        tr_description = traductor.traducir(description, original, idioma)
        tr_examples = traductor.traducir(examples, original, idioma)

        cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples, idioma)


def cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples, tr_idioma):
    ProcesamientoAgente.set_agente(rootdir, chat, 'displayName', tr_displayName)
    ProcesamientoAgente.set_agente(rootdir, chat, 'language', tr_idioma)
    ProcesamientoAgente.set_agente(rootdir, chat, 'shortDescription', tr_shortDescription)
    ProcesamientoAgente.set_agente(rootdir, chat, 'description', tr_description)
    ProcesamientoAgente.set_agente(rootdir, chat, 'examples', tr_examples)
