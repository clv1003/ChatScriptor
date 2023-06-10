import os
from transformers import pipeline

from traductor import Traductor
import ProcesamientoArchivos
import ProcesamientoAgente
import ProcesamientoEntidadesIntents

de_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", tokenizer="Helsinki-NLP/opus-mt-de-en")
de_es = pipeline("translation", model="Helsinki-NLP/opus-mt-de-es", tokenizer="Helsinki-NLP/opus-mt-de-es")
de_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-de-fr", tokenizer="Helsinki-NLP/opus-mt-de-fr")


def tr_de_en(chat, rootdir, original, idioma):
    chatbot = de_en(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_de_es(chat, rootdir, original, idioma):
    chatbot = de_es(chat)
    ProcesamientoArchivos.copiarDir(rootdir, chat, chatbot[0]['translation_text'])

    if os.path.exists(rootdir + chatbot[0]['translation_text']):
        traducirAgente(rootdir, chatbot[0]['translation_text'], original, idioma)
        return chatbot[0]['translation_text']


def tr_de_fr(chat, rootdir, original, idioma):
    chatbot = de_fr(chat)
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

        if idOrigen == 'de' and idDestino == 'en':
            tr_displayName = de_en(displayName)
            tr_shortDescription = de_en(shortDescription)
            tr_description = de_en(description)
            tr_examples = de_en(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'de' and idDestino == 'es':
            tr_displayName = de_es(displayName)
            tr_shortDescription = de_es(shortDescription)
            tr_description = de_es(description)
            tr_examples = de_es(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)

        elif idOrigen == 'de' and idDestino == 'fr':
            tr_displayName = de_fr(displayName)
            tr_shortDescription = de_fr(shortDescription)
            tr_description = de_fr(description)
            tr_examples = de_fr(examples)

            Traductor.cambiarIdioma(rootdir, chat, tr_displayName, tr_shortDescription,
                                    tr_description, tr_examples, idDestino)


def traducirEntidades(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        entidades = ProcesamientoEntidadesIntents.get_entidades(rootdir + chat)

        for entidad in entidades:
            datos = ProcesamientoEntidadesIntents.get_json(entidad[0], entidad[1])
            dirs = ProcesamientoEntidadesIntents.directoriosEntidad(rootdir + chat, entidad)

            if idOrigen == 'de' and idDestino == 'en':
                name = datos[0]['name']
                tr_name = de_en(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = de_en(value)
                    tr_synonyms = de_en(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = de_en(os.path.splitext(entidad[0])[0])
                nEntidad2 = de_en(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'de' and idDestino == 'es':
                name = datos[0]['name']
                tr_name = de_es(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = de_es(value)
                    tr_synonyms = de_es(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = de_es(os.path.splitext(entidad[0])[0])
                nEntidad2 = de_es(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')

            elif idOrigen == 'de' and idDestino == 'fr':
                name = datos[0]['name']
                tr_name = de_fr(name)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])

                for e in datos[1]:
                    value = e['value']
                    synonyms = e['synonyms']

                    tr_value = de_fr(value)
                    tr_synonyms = de_fr(synonyms)

                    ProcesamientoEntidadesIntents.editar_v_ent(rootdir + chat, value, entidad[0],
                                                               tr_value[0]['translation_text'])
                    ProcesamientoEntidadesIntents.editar_s_ent(rootdir + chat, synonyms, entidad[0],
                                                               tr_synonyms[0]['translation_text'])

                nEntidad1 = de_fr(os.path.splitext(entidad[0])[0])
                nEntidad2 = de_fr(os.path.splitext(entidad[1])[0])
                Traductor.traducirArchivo(rootdir, chat, entidad[0], entidad[1], nEntidad1 + ".json",
                                          nEntidad2 + ".json", 'entidad')


def traducirIntents(rootdir, chat, idOrigen, idDestino):
    if os.path.exists(rootdir + chat):
        intents = ProcesamientoEntidadesIntents.get_intents(rootdir + chat)

        for intent in intents:
            datos = ProcesamientoEntidadesIntents.get_json(intent[0], intent[1])
            dirs = ProcesamientoEntidadesIntents.directoriosIntent(rootdir + chat, intent)

            if idOrigen == 'de' and idDestino == 'en':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = de_en(name)
                tr_action = de_en(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = de_en(nombre)
                        tr_dataType = de_en(dataType)
                        tr_value = de_en(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = de_en(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = de_en(text)
                            tr_meta = de_en(meta)
                            tr_alias = de_en(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = de_en(os.path.splitext(intent[0])[0])
                nIntent2 = de_en(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'de' and idDestino == 'es':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = de_es(name)
                tr_action = de_es(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])
                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = de_es(nombre)
                        tr_dataType = de_es(dataType)
                        tr_value = de_es(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = de_es(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = de_es(text)
                            tr_meta = de_es(meta)
                            tr_alias = de_es(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = de_es(os.path.splitext(intent[0])[0])
                nIntent2 = de_es(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')

            elif idOrigen == 'de' and idDestino == 'fr':
                name = datos[0]['name']
                action = datos[0]['responses'][0]['action']
                tr_name = de_fr(name)
                tr_action = de_fr(action)
                ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_name[0]['translation_text'])
                ProcesamientoEntidadesIntents.editar_action(dirs[0], tr_action[0]['translation_text'])

                if datos[0]['responses'][0]['parameters']:
                    for i in datos[0]['responses'][0]['parameters']:
                        nombre = i['name']
                        dataType = i['dataType']
                        value = i['value']

                        tr_nombre = de_fr(nombre)
                        tr_dataType = de_fr(dataType)
                        tr_value = de_fr(value)

                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'name', tr_nombre[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'dataType',
                                                                    tr_dataType[0]['translation_text'])
                        ProcesamientoEntidadesIntents.editar_nombre(dirs[0], 'value', tr_value[0]['translation_text'])

                for i in datos[1]:
                    for j in i['data']:
                        if len(j) == 2:
                            text = j['text']
                            tr_text = de_fr(text)
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                        elif j['meta']:
                            text = j['text']
                            meta = j['meta']
                            alias = j['alias']

                            tr_text = de_fr(text)
                            tr_meta = de_fr(meta)
                            tr_alias = de_fr(alias)

                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'text',
                                                                           tr_text[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'meta',
                                                                           tr_meta[0]['translation_text'])
                            ProcesamientoEntidadesIntents.editar_responses(dirs[1], 'alias',
                                                                           tr_alias[0]['translation_text'])

                nIntent1 = de_fr(os.path.splitext(intent[0])[0])
                nIntent2 = de_fr(os.path.splitext(intent[1])[0])
                Traductor.traducirArchivo(rootdir, intent[0], intent[1], chat, nIntent1 + ".json", nIntent2 + ".json",
                                          'intent')
