import os
from transformers import pipeline

from traductor import Traductor
import ProcesamientoArchivos
import ProcesamientoAgente
import ProcesamientoEntidadesIntents

fr_en = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en", tokenizer="Helsinki-NLP/opus-mt-fr-en")
fr_es = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-es", tokenizer="Helsinki-NLP/opus-mt-fr-es")
fr_de = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-de", tokenizer="Helsinki-NLP/opus-mt-fr-de")


def tr_fr_en(chat, rootdir, original, idioma):
    chatbot = fr_en(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_fr_es(chat, rootdir, original, idioma):
    chatbot = fr_es(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_fr_de(chat, rootdir, original, idioma):
    chatbot = fr_de(chat)
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

        if idOrigen == 'fr' and idDestino == 'en':
            tr_displayName = fr_en(displayName)
            tr_shortDescription = fr_en(shortDescription)
            tr_description = fr_en(description)
            tr_examples = fr_en(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples,
                                    idDestino)

        elif idOrigen == 'fr' and idDestino == 'es':
            tr_displayName = fr_es(displayName)
            tr_shortDescription = fr_es(shortDescription)
            tr_description = fr_es(description)
            tr_examples = fr_es(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples,
                                    idDestino)

        elif idOrigen == 'fr' and idDestino == 'de':
            tr_displayName = fr_de(displayName)
            tr_shortDescription = fr_de(shortDescription)
            tr_description = fr_de(description)
            tr_examples = fr_de(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription, tr_description, tr_examples,
                                    idDestino)


def traducirEntidades(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat)

        for entidad in entidades:
            datos = ProcesamientoEntidadesIntents.get_json(entidad[0], entidad[1])
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad)

            if idOrigen == 'fr' and idDestino == 'en':
                name = datos[0]['name']
                tr_name = fr_en(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = fr_en(value)
                    tr_synonyms = fr_en(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = fr_en(os.path.splitext(entidad[0])[0])
                nEntidad2 = fr_en(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'fr' and idDestino == 'es':
                name = datos[0]['name']
                tr_name = fr_es(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = fr_es(value)
                    tr_synonyms = fr_es(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = fr_es(os.path.splitext(entidad[0])[0])
                nEntidad2 = fr_es(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'fr' and idDestino == 'de':
                name = datos[0]['name']
                tr_name = fr_de(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = fr_de(value)
                    tr_synonyms = fr_de(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = fr_de(os.path.splitext(entidad[0])[0])
                nEntidad2 = fr_de(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')


def traducirIntents(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat)

        for intent in intents:
            datos = ProcesamientoEntidadesIntents.get_json(intent[0], intent[1])
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent)

            if idOrigen == 'fr' and idDestino == 'en':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = fr_en(name)
                tr_action = fr_en(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = fr_en(nombre)
                        tr_dataType = fr_en(dataType)
                        tr_value = fr_en(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = fr_en(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = fr_en(text)
                            tr_meta = fr_en(meta)
                            tr_alias = fr_en(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = fr_en(os.path.splitext(intent[0])[0])
                nIntent2 = fr_en(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'fr' and idDestino == 'es':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = fr_es(name)
                tr_action = fr_es(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = fr_es(nombre)
                        tr_dataType = fr_es(dataType)
                        tr_value = fr_es(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = fr_es(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = fr_es(text)
                            tr_meta = fr_es(meta)
                            tr_alias = fr_es(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = fr_es(os.path.splitext(intent[0])[0])
                nIntent2 = fr_es(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'fr' and idDestino == 'de':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = fr_de(name)
                tr_action = fr_de(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = fr_de(nombre)
                        tr_dataType = fr_de(dataType)
                        tr_value = fr_de(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = fr_de(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = fr_de(text)
                            tr_meta = fr_de(meta)
                            tr_alias = fr_de(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = fr_de(os.path.splitext(intent[0])[0])
                nIntent2 = fr_de(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')
