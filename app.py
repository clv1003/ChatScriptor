from flask import Flask, render_template, url_for, redirect, request
from endpoints.datos import ProcesamientoDatosEndpoints

app = Flask(__name__)


# página inicial
@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


# página de inicio
@app.route('/login', methods=["GET"])
def login():
    return render_template("session/login.html")


# página con la información de creacion
@app.route('/about', methods=["GET"])
def about():
    return render_template("principal/about.html")


# --------------------------------------------------------------------------------------------------------
# página principal
@app.route('/inicio-sesion', methods=["GET"])
def paginaprincipalsesion():
    return render_template("principal/inicioSesion.html")


# página principal
@app.route('/inicio-no-sesion', methods=["GET"])
def paginaprincipalnosesion():
    return render_template("principal/inicioNoSesion.html", datos=ProcesamientoDatosEndpoints.get_disponible('./unzip'))


# --------------------------------------------------------------------------------------------------------
# ZONA DE PROCESAMIENTO DE DATOS AL IMPORTAR EL CHATBOT CON EL .ZIP
@app.route('/subir_archivo', methods=["POST"])
def procesar_archivo():
    ProcesamientoDatosEndpoints.descomprimir_archivo()
    return redirect(url_for('paginaprincipalnosesion'))


@app.route('/remove_unzip', methods=["GET"])
def remove_unzip():
    ProcesamientoDatosEndpoints.remove_unzip()
    return redirect(url_for('login'))


@app.route('/archivos')
def get_archivos():
    chat = request.args.get('chat')
    return render_template('principal/mostrar-datos/archivos.html',
                           arbol=ProcesamientoDatosEndpoints.get_arbol('./unzip/' + chat),
                           chat=chat)


@app.route('/agente')
def get_agente():
    chat = request.args.get('chat')
    return render_template("principal/mostrar-datos/agente.html",
                           agente=ProcesamientoDatosEndpoints.get_agente('./unzip/' + chat),
                           chat=chat)


@app.route('/entidades')
def get_entidades():
    chat = request.args.get('chat')
    return render_template("principal/mostrar-datos/entidades.html",
                           entidades=ProcesamientoDatosEndpoints.get_entidades('./unzip/' + chat),
                           chat=chat)


@app.route('/intents')
def get_intents():
    chat = request.args.get('chat')
    return render_template("principal/mostrar-datos/intents.html",
                           intents=ProcesamientoDatosEndpoints.get_intents('./unzip/' + chat),
                           chat=chat)


# --------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=False)
