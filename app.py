from flask import Flask, render_template, url_for, redirect
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


# página principal
@app.route('/inicio-sesion', methods=["GET"])
def paginaprincipalsesion():
    return render_template("principal/inicioSesion.html")


# página principal
@app.route('/inicio-no-sesion', methods=["GET"])
def paginaprincipalnosesion():
    return render_template("principal/inicioNoSesion.html")


# página con la información de creacion
@app.route('/about', methods=["GET"])
def about():
    return render_template("principal/about.html")


# --------------------------------------------------------------------------------------------------------
# ZONA DE PROCESAMIENTO DE DATOS AL IMPORTAR EL CHATBOT CON EL .ZIP
@app.route('/subir_archivo', methods=["POST"])
def procesar_archivo():
    ProcesamientoDatosEndpoints.descomprimir_archivo()
    return redirect(url_for('archivos'))


@app.route('/archivos')
def archivos():
    return render_template('principal/mostrar-datos/archivos.html',
                           arbol=ProcesamientoDatosEndpoints.get_arbol('./unzip'))


@app.route('/agente')
def agente():
    return render_template("principal/mostrar-datos/agente.html",
                           agente=ProcesamientoDatosEndpoints.get_agente('./unzip'))


@app.route('/entidades')
def entidades():
    return render_template("principal/mostrar-datos/entidades.html",
                           entidades=ProcesamientoDatosEndpoints.get_entidades('./unzip'))


@app.route('/intents')
def intents():
    return render_template("principal/mostrar-datos/intents.html",
                           intents=ProcesamientoDatosEndpoints.get_intents('./unzip'))


# --------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=False)
