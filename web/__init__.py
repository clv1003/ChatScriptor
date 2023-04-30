import os

from flask import Flask, render_template, url_for, redirect, request, session

import ProcesamientoAgente
import ProcesamientoArchivos
import ProcesamientoEntidadesIntents
import ProcesamientoZip
import ProcesamientoUsuario


def start_app():
    app = Flask(__name__)
    app.secret_key = 'estoesunaclavesecreta'

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
        if os.path.exists('./usuarios/' + session['email'] + '/'):
            return render_template("principal/home.html",
                                   datos=ProcesamientoArchivos.get_disponible('./usuarios/' + session['email'] + '/'),
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

        return redirect(url_for('login'))

    # para importar y exportar los archivos
    @app.route('/importar-exportar', methods=['GET'])
    def importacionexportacion():
        return render_template('principal/importar-exportar.html',
                               datos=ProcesamientoArchivos.get_disponible('./usuarios/' + session['email'] + '/'),
                               usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    # --------------------------------------------------------------------------------------------------------
    # ZONA DE PROCESAMIENTO DE DATOS AL IMPORTAR EL CHATBOT CON EL .ZIP
    @app.route('/subir_archivo', methods=["POST"])
    def procesar_archivo():
        ProcesamientoZip.descomprimir_archivo('./usuarios/' + session['email'] + '/')
        return redirect(url_for('importacionexportacion', rootdir='./usuarios/' + session['email'] + '/'))

    @app.route('/bajar_archivo', methods=["GET"])
    def obtener_zip():
        chat = request.args.get('chat')
        ProcesamientoZip.exportar_archivos('./usuarios/' + session['email'] + '/', chat)  # ./usuarios/{email}/Weather
        return redirect(url_for('importacionexportacion'))

    '''
        @app.route('/remove_unzip', methods=["POST"])
        def remove_unzip():
            ProcesamientoZip.remove_unzip()
            return redirect(url_for('login'))
    '''

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (OBTENCION DE INFORMACION)

    @app.route('/archivos/<string:chat>', methods=["GET"])
    def get_archivos(chat):
        return render_template('principal/mostrar-datos/archivos.html',
                               arbol=ProcesamientoArchivos.get_arbol('./usuarios/' + session['email'] + '/' + chat),
                               chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    # ------------------------
    # GET DATOS DEL AGENTE
    @app.route('/agente/<string:chat>', methods=["GET"])
    def get_agente(chat):
        return render_template("principal/mostrar-datos/agente.html",
                               agente=ProcesamientoAgente.get_agente('./usuarios/' + session['email'] + '/' + chat),
                               chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    # ------------------------
    # GET DATOS DEL ENTIDADES

    @app.route('/entidades/<string:chat>', methods=["GET"])
    def get_entidades(chat):
        return render_template("principal/mostrar-datos/entidades.html",
                               entidades=ProcesamientoEntidadesIntents.get_entidades(
                                   './usuarios/' + session['email'] + '/' + chat),
                               chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    @app.route('/entidades/<string:chat>/entidad/<string:entidad>', methods=["GET"])
    def get_entidad(chat, entidad):
        entidad = ProcesamientoArchivos.relistado(entidad)
        return render_template("principal/mostrar-datos/entidad.html",
                               ent=ProcesamientoEntidadesIntents.get_json(
                                   './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[0],
                                   './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[1]),
                               chat=chat, entidad=entidad[0],
                               usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    # ------------------------
    # GET DATOS DE INTENTS
    @app.route('/intents/<string:chat>', methods=["GET"])
    def get_intents(chat):
        return render_template("principal/mostrar-datos/intents.html",
                               intents=ProcesamientoEntidadesIntents.get_intents(
                                   './usuarios/' + session['email'] + '/' + chat),
                               chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    @app.route('/intents/<string:chat>/intent/<string:intent>', methods=["GET"])
    def get_intent(chat, intent):
        intent = ProcesamientoArchivos.relistado(intent)
        return render_template("principal/mostrar-datos/intent.html",
                               inte=ProcesamientoEntidadesIntents.get_json(
                                   './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[0],
                                   './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[1]),
                               chat=chat, intent=intent[0],
                               usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (MODIFICACION DE INFORMACION)
    # SET DATOS DEL AGENTE
    @app.route('/agente/editar/<string:chat>')
    def editar_agente(chat):
        return render_template("principal/modificar-datos/agente.html",
                               agente=ProcesamientoAgente.get_agente('./usuarios/' + session['email'] + '/' + chat),
                               chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

    @app.route('/actualizar_json', methods=["POST"])
    def actualizar_json():
        chat = request.args.get('chat')
        clave = request.args.get('clave')
        atributo = request.form['atributo']
        ProcesamientoAgente.set_agente('./usuarios/' + session['email'] + '/' + chat, clave, atributo)
        return redirect(url_for('get_agente', chat=chat))

    # --------------------------------------------------------------------------------------------------------

    # página login
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Verifica el usuario y la contraseña
            if ProcesamientoUsuario.verificar_usuario(email, password):
                rootdir = ProcesamientoUsuario.verificar_usuario(email, password)
                # Guarda el email en la sesión
                session['email'] = email
                return redirect(url_for('paginaprincipal', rootdir=rootdir))
            else:
                error = 'Usuario o contraseña incorrectos'
                return render_template('login.html', error=error)
        else:
            return render_template('login.html')

    # página de registro
    @app.route('/register', methods=["GET", "POST"])
    def register():
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']

            # Agrega el usuario al archivo CSV y crea un directorio para el usuario
            if ProcesamientoUsuario.registrar_usuario(nombre, email, password):
                return redirect(url_for('login'))
            else:
                error = 'El correo electrónico ya está en uso'
                return render_template('register.html', error=error)
        else:
            return render_template('register.html')

    @app.route('/logout')
    def logout():
        # Elimina el email de la sesión
        session.pop('email', None)
        return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------

    return app
