import ProcesamientoAgente
import ProcesamientoEntidadesIntents


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

    if len(resultados) == 0:
        return None

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
            if busqueda.lower() in e['value'] or busqueda.lower() in e['synonyms']:
                resultados2.append({"value": e['value'], "synonyms": e['synonyms']})

        return [resultados1, resultados2]

    # ------------- PARA EL INTENT
    if 'intents' in rootP1 and 'intents' in rootP2:
        # primer archivo intent
        name = parte1['name'].lower()
        action = parte1['responses'][0]['action'].lower()
        parameters = parte1['responses'][0]['parameters']

        if busqueda.lower() in name:
            resultados1.append('name')

        if busqueda.lower() in action:
            resultados1.append('responses')

        for i in parameters:
            if busqueda.lower() in i['name'].lower() or \
                    busqueda.lower() in i['dataType'].lower() or \
                    busqueda.lower() in i['value'].lower():
                resultados1.append({'responses': [{'parameters': i['id']}]})

        # segundo archivo de intent
        for j in parte2:
            for k in j['data']:
                if len(k) == 2:
                    if busqueda.lower() in k['text']:
                        resultados2.append({j['id']: 'data'})
                        break

                elif len(k) != 2 and (
                        busqueda.lower() in k['text'] or
                        busqueda.lower() in k['meta'] or
                        busqueda.lower() in k['alias']):
                    resultados2.append(j['id'])

        return [resultados1, resultados2]
