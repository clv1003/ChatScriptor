import ProcesamientoAgente
import ProcesamientoArchivos
import ProcesamientoEntidadesIntents
import ProcesamientoUsuario


# OBTENCION DEL VALOR BUSCADO EN EL AGENTE
def buscar_agente(root, busqueda):
    agente = ProcesamientoAgente.get_agente(root)

    displayName = agente['displayName'].lower()
    language = agente['language'].lower()
    shortDescription = agente['shortDescription'].lower()
    description = agente['description'].lower()
    examples = agente['examples'].lower()

    resultados = []

    if busqueda.lower() in displayName:
        resultados.append('displayName')

    if busqueda.lower() in language:
        resultados.append('language')

    if busqueda.lower() in shortDescription:
        resultados.append('shortDescription')

    if busqueda.lower() in description:
        resultados.append('description')

    if busqueda.lower() in examples:
        resultados.append('examples')

    if 'avatarUri' in agente:
        if busqueda.lower() in agente['avatarUri'].lower():
            resultados.append('avatarUri')

    return resultados


# OBTENCION DEL VALOR BUSCADO EN UNA ENTIDAD O EN UN INTENT
def buscar_ent_int(rootP1, rootP2, busqueda):
    resultados1 = []
    resultados2 = []
    parte1 = ProcesamientoEntidadesIntents.get_parte(rootP1)
    parte2 = ProcesamientoEntidadesIntents.get_parte(rootP2)

    # ------------- PARA LA ENTIDAD
    if 'entities' in rootP1 and 'entities' in rootP2:
        name = parte1['name'].lower()
        # primer archivo de entidad
        if busqueda.lower() in name:
            resultados1.append('name')

        # segundo archivo de entidad
        for e in parte2:
            if busqueda.lower() in e['value'].lower():
                resultados2.append({"value": e['value'], "synonyms": e['synonyms']})

            else:
                for s in e['synonyms']:
                    if busqueda.lower() in s.lower():
                        resultados2.append({"value": e['value'], "synonyms": e['synonyms']})
                        break

        return [resultados1, resultados2]

    # ------------- PARA EL INTENT
    if 'intents' in rootP1 and 'intents' in rootP2:
        # primer archivo intent
        name = parte1['name']
        action = parte1['responses'][0]['action']
        parameters = parte1['responses'][0]['parameters']
        messages = parte1['responses'][0]['messages'][0]

        if busqueda.lower() in name.lower():
            resultados1.append('name')

        if busqueda.lower() in action.lower():
            resultados1.append('responses')

        for i in parameters:
            if busqueda.lower() in i['name'].lower() or busqueda.lower() in i['dataType'].lower() or busqueda.lower() in i['value'].lower():
                if 'responses' not in resultados1:
                    resultados1.append('responses')

        if 'speech' in messages:
            lista = []
            for i in messages["speech"]:
                if busqueda.lower() in i.lower():
                    lista.append(i)

            if len(lista) > 0:
                resultados1.append({'speech': lista})

        # segundo archivo de intent
        for j in parte2:
            for k in j['data']:
                if len(k) == 2:
                    if busqueda.lower() in k['text'].lower():
                        resultados2.append(j['id'])
                        break
                elif len(k) != 2:
                    if busqueda.lower() in k['text'].lower() or busqueda.lower() in k['meta'].lower() or busqueda.lower() in k['alias'].lower():
                        resultados2.append(j['id'])

        return [resultados1, resultados2]


def buscar_entidades(dir_ents, busqueda):
    entidades = ProcesamientoEntidadesIntents.get_entidades(dir_ents)
    resultados = {}

    if not (entidades is None):
        for ent in entidades:
            root1 = dir_ents + '/entities/' + ent[0]
            root2 = dir_ents + '/entities/' + ent[1]

            if ent[0].endswith('.json'):
                e = ent[0].replace('.json', '')

                entity = buscar_ent_int(root1, root2, busqueda)
                resultados[e] = entity
    return resultados


def buscar_intents(dir_ints, busqueda):
    intents = ProcesamientoEntidadesIntents.get_intents(dir_ints)
    resultados = {}

    if not (intents is None):
        for inte in intents:
            root1 = dir_ints + '/intents/' + inte[0]
            root2 = dir_ints + '/intents/' + inte[1]

            if inte[0].endswith('.json'):
                i = inte[0].replace('.json', '')

                intent = buscar_ent_int(root1, root2, busqueda)
                resultados[i] = intent
    return resultados


def buscar_chatbot(directorio, busqueda):
    resultados = {'agente': None, 'entidades': None, 'intents': None}

    agente = buscar_agente(directorio, busqueda)
    intents = buscar_intents(directorio, busqueda)
    entidades = buscar_entidades(directorio, busqueda)

    resultados['agente'] = agente
    resultados['intents'] = intents
    resultados['entidades'] = entidades

    return resultados


def buscar_chatbots(directorio, busqueda):
    chatbots = ProcesamientoArchivos.get_disponible(directorio)
    resultados = {}

    for cb in chatbots:
        resultados[cb] = buscar_chatbot(directorio + '/' + cb, busqueda)

    return resultados


def buscar_usuarios(busqueda):
    usuarios = ProcesamientoUsuario.get_usuarios()
    resultados = []

    for u in usuarios:
        if busqueda.lower() in u.lower():
            resultados.append(u)

    return resultados
