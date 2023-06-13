import json
import os
import ProcesamientoAgente


# OBTENCIÓN DE LAS ENTIDADES DEL CHATBOT
def get_entidades(rootdir, language=None):
    if os.path.exists(rootdir + '/entities'):
        if language is None:
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
def get_intents(rootdir, language=None):
    if os.path.exists(rootdir + '/intents'):
        if language is None:
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
# OBTENER LOS DIRECTORIOS DE LOS ARCHIVOS
def directoriosEntidad(root, entidad, language=None):
    if entidad.endswith('.json'):
        entries1 = entidad
        if language is None:
            language = ProcesamientoAgente.get_agente_language(root)
        entidad = entidad.replace('.json', '')
        entries2 = entidad + '_entries_' + language + '.json'

        ent = [root + '/entities/' + entries1, root + '/entities/' + entries2]
        return ent


def directoriosIntent(root, intent, language=None):
    if intent.endswith('.json'):
        intent1 = intent
        if language is None:
            language = ProcesamientoAgente.get_agente_language(root)
        intent = intent.replace('.json', '')
        intent2 = intent + '_usersays_' + language + '.json'

        inte = [root + '/intents/' + intent1, root + '/intents/' + intent2]
        return inte


# ---------------------------------------------------------------------------------------------------------------------
# EDITAR EL NOMBRE DE ENTIDAD E INTENT
def editar_nombre(root, clave, atributo):
    diccionario = get_parte(root)
    diccionario[clave] = atributo

    with open(root, 'w') as e:
        json.dump(diccionario, e)


# ---------------------------------------------------------------------------------------------------------------------
# ELIMINAR ENTIDAD
def remove_entidad(root, chat, entidad, language=None):
    rootdir = root + chat + '/entities/'

    os.remove(rootdir + entidad)

    if language is None:
        language = ProcesamientoAgente.get_agente_language(root + chat)

    e = entidad.replace('.json', '')
    enti = e + '_entries_' + language + '.json'
    os.remove(rootdir + enti)


# ELIMINAR INTENT
def remove_intent(root, chat, intent, language=None):
    rootdir = root + chat + '/intents/'

    os.remove(rootdir + intent)

    if language is None:
        language = ProcesamientoAgente.get_agente_language(root + chat)

    i = intent.replace('.json', '')
    inte = i + '_usersays_' + language + '.json'
    os.remove(rootdir + inte)


# ---------------------------------------------------------------------------------------------------------------------
# EDITAR VALUE DE LAS ENTIDADES
def editar_v_ent(root, value, entidad, atributo, language=None):
    if entidad.endswith('.json'):
        if language is None:
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
def editar_s_ent(root, value, entidad, atributo, language=None):
    if entidad.endswith('.json'):
        if language is None:
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
def add_entry(root, entidad, value, synonyms, language=None):
    if entidad.endswith('.json'):
        if language is None:
            language = ProcesamientoAgente.get_agente_language(root)

        entidad = entidad.replace('.json', '')
        entries = entidad + '_entries_' + language + '.json'

        diccionario = get_parte(root + '/entities/' + entries)
        aux = {"value": value, "synonyms": synonyms}

        diccionario.append(aux)

        with open(root + '/entities/' + entries, 'w') as e:
            json.dump(diccionario, e)


# ELIMINAR ENTRADA DE ENTIDAD
def remove_entry(root, entidad, value, synonyms, language=None):
    if entidad.endswith('.json'):
        if language is None:
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
# AÑADIR MESSAGES A INTENTS
def add_messages(root, speach):
    diccionario = get_parte(root)

    if 'speech' in diccionario["responses"][0]["messages"][0]:
        diccionario["responses"][0]["messages"][0]["speech"].append(speach)
    else:
        diccionario["responses"][0]["messages"][0]["speech"] = []
        diccionario["responses"][0]["messages"][0]["speech"].append(speach)

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# EDITAR RESPONSES DE INTENTS
def editar_parameters(root, subclave, atributo):
    diccionario = get_parte(root)
    for i in diccionario["responses"][0]["parameters"]:
        if subclave in i:
            i[subclave] = atributo

    with open(root, 'w') as i:
        json.dump(diccionario, i)


def editar_action(root, atributo):
    diccionario = get_parte(root)
    if diccionario["responses"][0]["action"]:
        diccionario["responses"][0]["action"] = atributo

        with open(root, 'w') as i:
            json.dump(diccionario, i)


def editar_messages(root, speachOrg, speachNew):
    diccionario = get_parte(root)
    if diccionario["responses"][0]["messages"]:
        lista = []
        for j in diccionario["responses"][0]["messages"][0]["speech"]:
            if j == speachOrg:
                lista.append(speachNew)
            else:
                lista.append(j)

        diccionario["responses"][0]["messages"][0]["speech"] = lista

        with open(root, 'w') as i:
            json.dump(diccionario, i)


# ELIMINAR RESPONSES DE INTENTS
def remove_parameters(root, idR):
    diccionario = get_parte(root)

    for i in diccionario["responses"][0]["parameters"]:
        if i["id"] == idR:
            diccionario["responses"][0]["parameters"].remove(i)
            break

    with open(root, 'w') as i:
        json.dump(diccionario, i)


def remove_messages(root, speech):
    diccionario = get_parte(root)
    lista = []

    for j in diccionario["responses"][0]["messages"][0]["speech"]:
        if j != speech:
            lista.append(j)

    diccionario["responses"][0]["messages"][0]["speech"] = lista

    with open(root, 'w') as i:
        json.dump(diccionario, i)


# EDITAR DATA DE INTENTS
def editar_data(root, intent, old, tipo, atributo, language=None):
    if intent.endswith('.json'):
        stopflag = False
        if language is None:
            language = ProcesamientoAgente.get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for dt in diccionario:
            for d in dt["data"]:
                if len(d) == 2 and tipo == "text":
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break
                elif len(d) != 2 and (tipo == 'meta' or tipo == 'alias'):
                    if d[tipo] == old:
                        d[tipo] = atributo
                        stopflag = True
                        break

            if stopflag:
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)


# ELIMINAR DATA DE INTENTS
def remove_data(root, intent, idD, language=None):
    if intent.endswith('.json'):
        if language is None:
            language = ProcesamientoAgente.get_agente_language(root)
        intent = intent.replace('.json', '')
        data = intent + '_usersays_' + language + '.json'

        diccionario = get_parte(root + '/intents/' + data)

        for i in diccionario:
            if i["id"] == idD:
                diccionario.remove(i)
                break

        with open(root + '/intents/' + data, 'w') as i:
            json.dump(diccionario, i)
