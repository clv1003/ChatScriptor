import json
import os
import ProcesamientoAgente


# OBTENCIÓN DE LAS ENTIDADES DEL CHATBOT
def get_entidades(rootdir):
    if os.path.exists(rootdir + '/entities'):
        language = ProcesamientoAgente.get_agente_language(rootdir)
        archivos = os.listdir(rootdir + '/entities')
        agrupados = []

        for archivo in archivos:
            if archivo.endswith('.json'):
                entity = archivo.replace('.json', '')
                entries = entity + '_entries_' + language + '.json'
                if entries in archivos:
                    agrupados.append([archivo, entries])

        return agrupados
    else:
        return None


# OBTENCIÓN DE LOS INTENTS DEL CHATBOT
def get_intents(rootdir):
    if os.path.exists(rootdir + '/intents'):
        language = ProcesamientoAgente.get_agente_language(rootdir)
        archivos = os.listdir(rootdir + '/intents')
        agrupados = []

        for archivo in archivos:
            if archivo.endswith('.json'):
                intent = archivo.replace('.json', '')
                usersays = intent + '_usersays_' + language + '.json'
                if usersays in archivos:
                    agrupados.append([archivo, usersays])

        return agrupados
    else:
        return None


def get_json(parte1, parte2):
    part1 = get_parte(parte1)
    part2 = get_parte(parte2)

    return [part1, part2]


def get_parte(parte):
    if os.path.exists(parte):
        with open(parte, 'r', encoding='utf-8') as p:
            p = json.load(p)

            return p
    else:
        return None


def editar_nombre(root, clave, atributo):
    diccionario = get_parte(root)
    diccionario[clave] = atributo

    with open(root, 'w') as e:
        json.dump(diccionario, e)


def remove_entidad(root, chat, entidad):
    rootdir = root + chat + '/entities/'

    os.remove(rootdir + entidad)

    e = entidad.replace('.json', '')
    enti = e + '_entries_' + ProcesamientoAgente.get_agente_language(root + chat) + '.json'
    os.remove(rootdir + enti)


def remove_intent(root, chat, intent):
    rootdir = root + chat + '/intents/'

    os.remove(rootdir + intent)

    i = intent.replace('.json', '')
    inte = i + '_usersays_' + ProcesamientoAgente.get_agente_language(root + chat) + '.json'
    os.remove(rootdir + inte)


def editar_v_ent(root, value, entidad, atributo):
    if entidad.endswith('.json'):
        language = ProcesamientoAgente.get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)

        for d in diccionario:
            if d["value"] == value:
                d["value"] = atributo

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


def editar_s_ent(root, value, entidad, atributo):
    if entidad.endswith('.json'):
        language = ProcesamientoAgente.get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)

        for d in diccionario:
            if d["value"] == value:
                d["synonyms"] = atributo

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


def add_entry(root, entidad, value, synonyms):
    if entidad.endswith('.json'):
        language = ProcesamientoAgente.get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)
        aux = {"value": value, "synonyms": synonyms}

        diccionario.append(aux)

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


def remove_entry(root, entidad, value, synonyms):
    if entidad.endswith('.json'):
        language = ProcesamientoAgente.get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)
        for d in diccionario:
            if d["value"] == value and d["synonyms"] == synonyms:
                diccionario.remove(d)

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)
