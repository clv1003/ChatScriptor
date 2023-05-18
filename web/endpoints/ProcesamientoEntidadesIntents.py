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


# ---------------------------------------------------------------------------------------------------------------------
# AGRUPAR LOS DOS TIPOS DE JSON
def get_json(parte1, parte2):
    part1 = get_parte(parte1)
    part2 = get_parte(parte2)

    return [part1, part2]


# OBTENER LOS DATOS DE LOS JSON
def get_parte(parte):
    if os.path.exists(parte):
        with open(parte, 'r', encoding='utf-8') as p:
            p = json.load(p)

            return p
    else:
        return None


# ---------------------------------------------------------------------------------------------------------------------
# EDITAR EL NOMBRE DE ENTIDAD E INTENT
def editar_nombre(root, clave, atributo):
    diccionario = get_parte(root)
    diccionario[clave] = atributo

    with open(root, 'w') as e:
        json.dump(diccionario, e)


# ---------------------------------------------------------------------------------------------------------------------
# ELIMINAR ENTIDAD
def remove_entidad(root, chat, entidad):
    rootdir = root + chat + '/entities/'

    os.remove(rootdir + entidad)

    e = entidad.replace('.json', '')
    enti = e + '_entries_' + ProcesamientoAgente.get_agente_language(root + chat) + '.json'
    os.remove(rootdir + enti)


# ELIMINAR INTENT
def remove_intent(root, chat, intent):
    rootdir = root + chat + '/intents/'

    os.remove(rootdir + intent)

    i = intent.replace('.json', '')
    inte = i + '_usersays_' + ProcesamientoAgente.get_agente_language(root + chat) + '.json'
    os.remove(rootdir + inte)


# ---------------------------------------------------------------------------------------------------------------------
# EDITAR VALUE DE LAS ENTIDADES
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


# EDITAR SYNONYMS DE LAS ENTIDADES
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


# AÑADIR UNA NUEVA ENTRADA DE ENTIDAD
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


# ELIMINAR ENTRADA DE ENTIDAD
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


# ---------------------------------------------------------------------------------------------------------------------
# EDITAR RESPONSES DE INTENTS
def editar_responses(root, subclave, atributo):
    diccionario = get_parte(root)
    for i in diccionario["responses"][0]["parameters"]:
        if subclave in i:
            i[subclave] = atributo

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# AÑADIR RESPONSES DE INTENTS
def add_responses(root, name, dataType, value):
    pass


# ELIMINAR RESPONSES DE INTENTS
def remove_responses(root, idR):
    diccionario = get_parte(root)

    for i in diccionario["responses"][0]["parameters"]:
        if i["id"] == idR:
            diccionario["responses"][0]["parameters"].remove(i)
            break

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# EDITAR DATA DE INTENTS
def editar_data(root, intent, old, tipo, atributo):
    if intent.endswith('.json'):
        stopflag = False
        language = ProcesamientoAgente.get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for dt in diccionario:
            for d in dt["data"]:
                if len(d) == 2 and tipo == "text":
                    print(f'text')
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break
                elif len(d) != 2 and (tipo == 'meta' or tipo == 'alias'):
                    print(f'meta o alias')
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break

            if stopflag:
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)


# ELIMINAR DATA DE INTENTS
def remove_data(root, intent, idD):
    if intent.endswith('.json'):
        print(f'id -> {idD}')
        language = ProcesamientoAgente.get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for i in diccionario:
            print(f'{i["id"]} == {idD} -- {i["id"] == idD}')
            if i["id"] == idD:
                diccionario.remove(i)
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)
