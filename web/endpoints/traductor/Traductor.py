# IMPORTS
from transformers import MarianMTModel, MarianTokenizer

'''
CLASE TRADUCTOR
@Author: Claudia Landeira

Funciones encargadas de realizar la traduccion del bloque de intents
'''


# CLASE --> Traductor
# Clase adaptador que hace uso de los modelos de traduccion de Hugging Face para realizar el proceso de traudccion
class Traductor:
    # Inicializar la clase Traductor
    def __init__(self, original, idioma):
        modelos = {
            'en-es': {
                'model_name': 'Helsinki-NLP/opus-mt-en-es',
                'tokenizer_name': 'Helsinki-NLP/opus-mt-en-es'
            },
            'es-en': {
                'model_name': 'Helsinki-NLP/opus-mt-es-en',
                'tokenizer_name': 'Helsinki-NLP/opus-mt-es-en'
            }
        }

        model_name = modelos[f'{original}-{idioma}']['model_name']
        tokenizer_name = modelos[f'{original}-{idioma}']['tokenizer_name']

        self.modelo = MarianMTModel.from_pretrained(model_name)
        self.token = MarianTokenizer.from_pretrained(tokenizer_name)

        self.original = original
        self.idioma = idioma

    # FUNCION --> getOriginal
    # Funcion encargada de la obtencion del idioma original del chatbot
    def getOriginal(self):
        return self.original

    # FUNCION --> getIdioma
    # Funcion encargada de la obtencion del idioma al que se va a traducir el chatbot
    def getIdioma(self):
        return self.idioma

    # FUNCION --> traducirFrase
    # Funcion encargada de la traduccion de frases o palabras
    def traducirFrase(self, frase, max_length=512):
        input = self.token(frase, return_tensors='pt')
        input_ids = input['input_ids']
        attention_mask = input['attention_mask']

        tr_model = self.modelo.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=max_length)
        tr_token = self.token.decode(tr_model[0], skip_special_tokens=True)

        return tr_token

    # FUNCION --> traducirDiccionario
    # Funcion encargada de la traduccion de diccionarios
    def traducirDiccionario(self, diccionario):
        tr_diccionario = {}

        for clave, frase in diccionario.items():
            tr_frase = self.traducirFrase(frase)
            tr_diccionario[clave] = tr_frase

        return tr_diccionario
