# https://googleapis.dev/python/google-auth/1.7.0/reference/google.auth.transport.requests.html
import google.auth.exceptions
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport import requests as google_request
from googleapiclient.discovery import build

'''
def get_user_info(access_token):
    try:
        idinfo = id_token.verify_oauth2_token(access_token, google_request.Request(), client_id)

        name = idinfo['name']
        email = idinfo['email']

        return {'name': name, 'email': email}
    except google.auth.exceptions.TransportError as e:
        return 'Error de transporte: ' + str(e)
    except ValueError as e:
        return 'Error al verificar el token: ' + str(e)
'''


def get_user_info(token):
    userinfo_endpoint = 'https://www.googleapis.com/oauth2/v3/userinfo'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(userinfo_endpoint, headers=headers)
    print(f'Response: {response.text}')
    if response.status_code == 200:
        userinfo_data = response.json()
        user_info = {
            'name': userinfo_data.get('name'),
            'email': userinfo_data.get('email')
        }
        return user_info
    else:
        print(f'Error al obtener información del usuario: {response.status_code} - {response.text}')
        return None
