import os
from transformers import pipeline

from traductor import Traductor
import ProcesamientoArchivos
import ProcesamientoAgente
import ProcesamientoEntidadesIntents

en_es = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es", tokenizer="Helsinki-NLP/opus-mt-en-es")
en_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr", tokenizer="Helsinki-NLP/opus-mt-en-fr")
en_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", tokenizer="Helsinki-NLP/opus-mt-en-de")


def tr_en_es(chat, rootdir, original, idioma):
    chatbot = en_es(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_en_fr(chat, rootdir, original, idioma):
    chatbot = en_fr(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_en_de(chat, rootdir, original, idioma):
    chatbot = en_de(chat)
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

        if idOrigen == 'en' and idDestino == 'es':
            tr_displayName = en_es(displayName)
            tr_shortDescription = en_es(shortDescription)
            tr_description = en_es(description)
            tr_examples = en_es(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'en' and idDestino == 'fr':
            tr_displayName = en_fr(displayName)
            tr_shortDescription = en_fr(shortDescription)
            tr_description = en_fr(description)
            tr_examples = en_fr(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'en' and idDestino == 'de':
            tr_displayName = en_de(displayName)
            tr_shortDescription = en_de(shortDescription)
            tr_description = en_de(description)
            tr_examples = en_de(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)


def traducirEntidades(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat)

        for entidad in entidades:
            datos = ProcesamientoEntidadesIntents.get_json(entidad[0], entidad[1])
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad)

            if idOrigen == 'en' and idDestino == 'es':
                name = datos[0]['name']
                tr_name = en_es(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = en_es(value)
                    tr_synonyms = en_es(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = en_es(os.path.splitext(entidad[0])[0])
                nEntidad2 = en_es(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'en' and idDestino == 'fr':
                name = datos[0]['name']
                tr_name = en_fr(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = en_fr(value)
                    tr_synonyms = en_fr(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = en_fr(os.path.splitext(entidad[0])[0])
                nEntidad2 = en_fr(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'en' and idDestino == 'de':
                name = datos[0]['name']
                tr_name = en_de(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = en_de(value)
                    tr_synonyms = en_de(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = en_de(os.path.splitext(entidad[0])[0])
                nEntidad2 = en_de(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')


def traducirIntents(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat)

        for intent in intents:
            datos = ProcesamientoEntidadesIntents.get_json(intent[0], intent[1])
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent)

            if idOrigen == 'en' and idDestino == 'es':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = en_es(name)
                tr_action = en_es(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = en_es(nombre)
                        tr_dataType = en_es(dataType)
                        tr_value = en_es(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = en_es(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = en_es(text)
                            tr_meta = en_es(meta)
                            tr_alias = en_es(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = en_es(os.path.splitext(intent[0])[0])
                nIntent2 = en_es(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'en' and idDestino == 'fr':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = en_fr(name)
                tr_action = en_fr(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = en_fr(nombre)
                        tr_dataType = en_fr(dataType)
                        tr_value = en_fr(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = en_fr(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = en_fr(text)
                            tr_meta = en_fr(meta)
                            tr_alias = en_fr(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = en_fr(os.path.splitext(intent[0])[0])
                nIntent2 = en_fr(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'en' and idDestino == 'de':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = en_de(name)
                tr_action = en_de(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = en_de(nombre)
                        tr_dataType = en_de(dataType)
                        tr_value = en_de(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = en_es(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = en_de(text)
                            tr_meta = en_de(meta)
                            tr_alias = en_de(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = en_de(os.path.splitext(intent[0])[0])
                nIntent2 = en_de(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')
