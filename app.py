import os
import requests
from flask import Flask, render_template, url_for, redirect, request
# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session

from endpoints.datos import ProcesamientoDatosEndpoints
# from endpoints import DatosGoogle

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Datos de la aplicacion de Google Cloud
CLIENT_ID = '203629964308-r0d5li2dpeo90u4ov51vdqrhvh1cvh1r.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:5000/google_login_callback'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
# Datos del proyecto de Dialogflow
PROJECT_ID = 'tfg-dialogflow-clv'
SCOPES = ['https://www.googleapis.com/auth/dialogflow']


# cliente = BackendApplicationClient(client_id=CLIENT_ID)
# oauth = OAuth2Session(client=cliente, redirect_uri=REDIRECT_URI)


# --------------------------------------------------------------------------------------------------------

@app.route('/google_login')
def google_login():
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={"".join(SCOPES)}'
    return redirect(auth_url)


@app.route('/google_login_callback')
def google_login_callback():
    '''
    code = request.args.get('code')
    token = oauth.fetch_token(token_url=TOKEN_URL,
                              client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET,
                              code=code,
                              grant_type='authorization_code',
                              scopes=SCOPES)

    if not isinstance(token, dict):
        return 'Error: Token no válido'

    access_token = token['access_token']

    chatbots = ProcesamientoDatosEndpoints.get_chatbots(access_token, PROJECT_ID)
    user_info = DatosGoogle.get_user_info(access_token, CLIENT_ID)
    '''

    code = request.args.get('code')
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
        'scopes': SCOPES
    }
    response = requests.post(TOKEN_URL, data=data)
    token = response.json()

    if not isinstance(token, dict):
        return 'Error: Token no valido'

    access_token = token['access_token']

    chatbots = ProcesamientoDatosEndpoints.get_chatbots(access_token, PROJECT_ID)
    # user_info = DatosGoogle.get_user_info(access_token)

    return render_template("principal/inicioSesion.html", chatbots=chatbots)  # , user_info=user_info)


# --------------------------------------------------------------------------------------------------------
# ORGANIZAICIÓN DE LAS PÁGINAS

# página con la pantalla de carga
@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


# página de inicio de sesion
@app.route('/login', methods=["GET"])
def login():
    return render_template("session/login.html")


# página con la información de creacion
@app.route('/about', methods=["GET"])
def about():
    return render_template("principal/about.html")


# página principal inicio de sesion con Google (aun no funciona)
'''
@app.route('/inicio-sesion')
def paginaprincipalsesion():
    if 'credentials' in session:
        user_info = DatosGoogle.get_user_info()
        chatbots = ProcesamientoDatosEndpoints.get_chatbots(PROJECT_ID)
        return render_template("principal/inicioSesion.html", chatbots=chatbots, user_info=user_info)

    return redirect(url_for('login'))
'''


# página principal no sesion
@app.route('/inicio-no-sesion', methods=["GET"])
def paginaprincipalnosesion():
    return render_template("principal/inicioNoSesion.html",
                           datos=ProcesamientoDatosEndpoints.get_disponible('./unzip'))


# para importar y exportar los archivos
@app.route('/importar-exportar', methods=['GET'])
def importacionexportacion():
    return render_template('principal/importar-exportar.html',
                           datos=ProcesamientoDatosEndpoints.get_disponible('./unzip'))


# --------------------------------------------------------------------------------------------------------
# ZONA DE PROCESAMIENTO DE DATOS AL IMPORTAR EL CHATBOT CON EL .ZIP
@app.route('/subir_archivo', methods=["POST"])
def procesar_archivo():
    ProcesamientoDatosEndpoints.descomprimir_archivo()
    return redirect(url_for('paginaprincipalnosesion'))


@app.route('/bajar_archivo', methods=["GET"])
def obtener_zip():
    chat = request.args.get('chat')
    ProcesamientoDatosEndpoints.exportar_archivos('./unzip/', chat)  # ./unzip/Weather
    return redirect(url_for('importacionexportacion'))


@app.route('/remove_unzip', methods=["POST"])
def remove_unzip():
    ProcesamientoDatosEndpoints.remove_unzip()
    return redirect(url_for('login'))


# --------------------------------------------------------------------------------------------------------
# TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (OBTENCION DE INFORMACION)

@app.route('/archivos/<string:chat>', methods=["GET"])
def get_archivos(chat):
    return render_template('principal/mostrar-datos/archivos.html',
                           arbol=ProcesamientoDatosEndpoints.get_arbol('./unzip/' + chat),
                           chat=chat)


# ------------------------
# GET DATOS DEL AGENTE
@app.route('/agente/<string:chat>', methods=["GET"])
def get_agente(chat):
    return render_template("principal/mostrar-datos/agente.html",
                           agente=ProcesamientoDatosEndpoints.get_agente('./unzip/' + chat),
                           chat=chat)


# ------------------------
# GET DATOS DEL ENTIDADES

@app.route('/entidades/<string:chat>', methods=["GET"])
def get_entidades(chat):
    return render_template("principal/mostrar-datos/entidades.html",
                           entidades=ProcesamientoDatosEndpoints.get_entidades('./unzip/' + chat),
                           chat=chat)


@app.route('/entidades/<string:chat>/entidad/<string:entidad>', methods=["GET"])
def get_entidad(chat, entidad):
    return render_template("principal/mostrar-datos/entidad.html",
                           ent=ProcesamientoDatosEndpoints.get_entidad(
                               './unzip/' + chat + '/entities/' + entidad),
                           chat=chat, entidad=entidad)


@app.route('/entidades/<string:chat>/entidade/<string:entidad>', methods=["GET"])
def get_entidad_entries(chat, entidad):
    return render_template("principal/mostrar-datos/entidad.html",
                           ent=ProcesamientoDatosEndpoints.get_entidad_entries(
                               './unzip/' + chat + '/entities/' + entidad),
                           chat=chat, entidad=entidad)


# ------------------------
# GET DATOS DE INTENTS
@app.route('/intents/<string:chat>', methods=["GET"])
def get_intents(chat):
    return render_template("principal/mostrar-datos/intents.html",
                           intents=ProcesamientoDatosEndpoints.get_intents('./unzip/' + chat),
                           chat=chat)


@app.route('/intents/<string:chat>/intent/<string:intent>', methods=["GET"])
def get_intent(chat, intent):
    return render_template("principal/mostrar-datos/intent.html",
                           inte=ProcesamientoDatosEndpoints.get_intent('./unzip/' + chat + '/intents/' + intent),
                           chat=chat, intent=intent)


@app.route('/intents/<string:chat>/intentu/<string:intent>', methods=["GET"])
def get_intent_usersays(chat, intent):
    return render_template("principal/mostrar-datos/intent.html",
                           inte=ProcesamientoDatosEndpoints.get_intent_usersays(
                               './unzip/' + chat + '/intents/' + intent),
                           chat=chat, intent=intent)


# --------------------------------------------------------------------------------------------------------
# TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (MODIFICACION DE INFORMACION)
# SET DATOS DEL AGENTE
@app.route('/agente/editar/<string:chat>')
def editar_agente(chat):
    return render_template("principal/modificar-datos/agente.html",
                           agente=ProcesamientoDatosEndpoints.get_agente('./unzip/' + chat),
                           chat=chat)


@app.route('/actualizar_json', methods=["POST"])
def actualizar_json(chat, clave):
    ProcesamientoDatosEndpoints.set_agente('./unzip/' + chat, clave)
    return redirect(url_for('get_agente', chat=chat))


# --------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run(debug=False)
