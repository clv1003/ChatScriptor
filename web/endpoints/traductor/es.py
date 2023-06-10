import os
from transformers import pipeline

from traductor import Traductor
import ProcesamientoArchivos
import ProcesamientoAgente
import ProcesamientoEntidadesIntents

es_en = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en", tokenizer="Helsinki-NLP/opus-mt-es-en")
es_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-es-fr", tokenizer="Helsinki-NLP/opus-mt-es-fr")
es_de = pipeline("translation", model="Helsinki-NLP/opus-mt-es-de", tokenizer="Helsinki-NLP/opus-mt-es-de")


def tr_es_en(chat, rootdir, original, idioma):
    chatbot = es_en(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_es_fr(chat, rootdir, original, idioma):
    chatbot = es_fr(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_es_de(chat, rootdir, original, idioma):
    chatbot = es_de(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def traducirAgente(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        agente = ProcesamientoAgente.get_agente(rootdir + chat)

        displayName = agente['displayName']
        shortDescription = agente['shortDescription']
        description = agente['description']
        examples = agente['examples']

        if idOrigen == 'es' and idDestino == 'en':
            tr_displayName = es_en(displayName)
            tr_shortDescription = es_en(shortDescription)
            tr_description = es_en(description)
            tr_examples = es_en(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'es' and idDestino == 'fr':
            tr_displayName = es_fr(displayName)
            tr_shortDescription = es_fr(shortDescription)
            tr_description = es_fr(description)
            tr_examples = es_fr(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'es' and idDestino == 'de':
            tr_displayName = es_de(displayName)
            tr_shortDescription = es_de(shortDescription)
            tr_description = es_de(description)
            tr_examples = es_de(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)


def traducirEntidades(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat)

        for entidad in entidades:
            datos = ProcesamientoEntidadesIntents.get_json(entidad[0], entidad[1])
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad)

            if idOrigen == 'es' and idDestino == 'en':
                name = datos[0]['name']
                tr_name = es_en(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = es_en(value)
                    tr_synonyms = es_en(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = es_en(os.path.splitext(entidad[0])[0])
                nEntidad2 = es_en(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'es' and idDestino == 'fr':
                name = datos[0]['name']
                tr_name = es_fr(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = es_fr(value)
                    tr_synonyms = es_fr(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = es_fr(os.path.splitext(entidad[0])[0])
                nEntidad2 = es_fr(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'es' and idDestino == 'de':
                name = datos[0]['name']
                tr_name = es_de(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = es_de(value)
                    tr_synonyms = es_de(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = es_de(os.path.splitext(entidad[0])[0])
                nEntidad2 = es_de(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')


def traducirIntents(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat)

        for intent in intents:
            datos = ProcesamientoEntidadesIntents.get_json(intent[0], intent[1])
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent)

            if idOrigen == 'es' and idDestino == 'en':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = es_en(name)
                tr_action = es_en(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = es_en(nombre)
                        tr_dataType = es_en(dataType)
                        tr_value = es_en(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = es_en(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = es_en(text)
                            tr_meta = es_en(meta)
                            tr_alias = es_en(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = es_en(os.path.splitext(intent[0])[0])
                nIntent2 = es_en(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'es' and idDestino == 'fr':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = es_fr(name)
                tr_action = es_fr(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = es_fr(nombre)
                        tr_dataType = es_fr(dataType)
                        tr_value = es_fr(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = es_fr(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = es_fr(text)
                            tr_meta = es_fr(meta)
                            tr_alias = es_fr(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = es_fr(os.path.splitext(intent[0])[0])
                nIntent2 = es_fr(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'es' and idDestino == 'de':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = es_de(name)
                tr_action = es_de(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = es_de(nombre)
                        tr_dataType = es_de(dataType)
                        tr_value = es_de(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = es_de(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = es_de(text)
                            tr_meta = es_de(meta)
                            tr_alias = es_de(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = es_de(os.path.splitext(intent[0])[0])
                nIntent2 = es_de(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')
