from flask import Flask, render_template, url_for, redirect, request
from endpoints.datos import ProcesamientoDatosEndpoints

app = Flask(__name__)


# --------------------------------------------------------------------------------------------------------
# ORGANIZAICIÓN DE LAS PÁGINAS

# página con la pantalla de carga
@app.route('/', methods=["GET"])
def home():
    return render_template('paginacarga.html')


# página con la información de creacion
@app.route('/about', methods=["GET"])
def about():
    return render_template("principal/about.html")


# página principal no sesion
@app.route('/home', methods=["GET"])
def paginaprincipal():
    return render_template("principal/home.html",
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
    return redirect(url_for('importacionexportacion'))


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
def actualizar_json():
    chat = request.args.get('chat')
    clave = request.args.get('clave')
    ProcesamientoDatosEndpoints.set_agente('./unzip/' + chat, clave)
    return redirect(url_for('get_agente', chat=chat))


# --------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run(debug=False)
