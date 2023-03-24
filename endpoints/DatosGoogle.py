# https://googleapis.dev/python/google-auth/1.7.0/reference/google.auth.transport.requests.html
from google.auth.credentials import Credentials
from google.oauth2 import id_token
from google.auth.transport import requests
from endpoints.datos import ProcesamientoDatosEndpoints


def googleLogin(token, client_id, project_id):
    try:
        info = id_token.verify_oauth2_token(token, requests.Request(), client_id)

        # google_id = info['sub']
        # google_email = info['email']
        # google_name = info['name']

        credenciales = Credentials.from_authorized_user_info(info)

        chatbots = ProcesamientoDatosEndpoints.get_chatbots(project_id, credenciales)
        return chatbots

    except ValueError:
        return "Invalid token"


'''
# -----------------------------------------------------------------------------------------------------
# Obtener la url para cada request

urlGeneral = 'https://dialogflow.googleapis.com/v2/projects/tfg-dialogflow-clv/agent'


def obtenerURL(tipo):
    if tipo == 1:  # Agente
        return urlGeneral

    if tipo == 2:  # Fulfillment
        return urlGeneral + '/fulfillment'

    if tipo == 3:  # Validation Result
        return urlGeneral + '/validationResult'

    if tipo == 4:  # entity types
        return urlGeneral + '/entityTypes'

    if tipo == 5:  # enviroments
        return urlGeneral + '/enviroments'

    return None


# -----------------------------------------------------------------------------------------------------
# Obtener el token de autenticacion para poder acceder y hacer peticiones

def obtenerToken():
    # Cargar las credenciales de la cuenta de servicio
    credenciales = service_account.Credentials.from_service_account_file('json/client_secret.json')

    # Obtener el token de acceso
    auth_request = google.auth.transport.requests.Request()
    credenciales.refresh(auth_request)
    token_acceso = credenciales.token

    return token_acceso
'''
