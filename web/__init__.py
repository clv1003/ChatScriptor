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
        if 'email' in session:
            return render_template("principal/about.html")
        else:
            return redirect(url_for('login'))

    # página principal no sesion
    @app.route('/home/', methods=["GET"])
    def paginaprincipal():
        if 'email' in session:
            if os.path.exists('./usuarios/' + session['email'] + '/'):
                return render_template("principal/home.html",
                                       datos=ProcesamientoArchivos.get_disponible(
                                           './usuarios/' + session['email'] + '/'),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
            return redirect(url_for('login'))

        else:
            return redirect(url_for('login'))

    @app.route('/admin', methods=["GET"])
    def paginaprincipaladmin():
        if 'email' in session:
            if os.path.exists('./usuarios'):
                return render_template("principal/admin.html",
                                       datos=ProcesamientoArchivos.get_disponible('./usuarios'),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # para importar y exportar los archivos
    @app.route('/importar-exportar', methods=['GET'])
    def importacionexportacion():
        if 'email' in session:
            return render_template('principal/importar-exportar.html',
                                   datos=ProcesamientoArchivos.get_disponible('./usuarios/' + session['email'] + '/'),
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    # ZONA DE PROCESAMIENTO DE DATOS AL IMPORTAR EL CHATBOT CON EL .ZIP
    @app.route('/subir_archivo', methods=["POST"])
    def procesar_archivo():
        if 'email' in session:
            ProcesamientoZip.descomprimir_archivo('./usuarios/' + session['email'] + '/')
            return redirect(url_for('importacionexportacion', rootdir='./usuarios/' + session['email'] + '/'))
        else:
            return redirect(url_for('login'))

    @app.route('/bajar_archivo', methods=["GET"])
    def obtener_zip():
        if 'email' in session:
            chat = request.args.get('chat')
            ProcesamientoZip.exportar_archivos('./usuarios/' + session['email'] + '/',
                                               chat)  # ./usuarios/{email}/Weather
            return redirect(url_for('importacionexportacion'))
        else:
            return redirect(url_for('login'))

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
        if 'email' in session:
            return render_template('principal/mostrar-datos/archivos.html',
                                   arbol=ProcesamientoArchivos.get_arbol('./usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # GET DATOS DEL AGENTE
    @app.route('/agente/<string:chat>', methods=["GET"])
    def get_agente(chat):
        if 'email' in session:
            return render_template("principal/mostrar-datos/agente.html",
                                   agente=ProcesamientoAgente.get_agente('./usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # GET DATOS DEL ENTIDADES

    @app.route('/entidades/<string:chat>', methods=["GET"])
    def get_entidades(chat):
        if 'email' in session:
            return render_template("principal/mostrar-datos/entidades.html",
                                   entidades=ProcesamientoEntidadesIntents.get_entidades(
                                       './usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/entidades/<string:chat>/entidad/<string:entidad>', methods=["GET"])
    def get_entidad(chat, entidad):
        if 'email' in session:
            entidad = ProcesamientoArchivos.relistado(entidad)
            return render_template("principal/mostrar-datos/entidad.html",
                                   ent=ProcesamientoEntidadesIntents.get_json(
                                       './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[0],
                                       './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[1]),
                                   chat=chat, entidad=entidad[0],
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # GET DATOS DE INTENTS
    @app.route('/intents/<string:chat>', methods=["GET"])
    def get_intents(chat):
        if 'email' in session:
            return render_template("principal/mostrar-datos/intents.html",
                                   intents=ProcesamientoEntidadesIntents.get_intents(
                                       './usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/intents/<string:chat>/intent/<string:intent>', methods=["GET"])
    def get_intent(chat, intent):
        if 'email' in session:
            intent = ProcesamientoArchivos.relistado(intent)
            return render_template("principal/mostrar-datos/intent.html",
                                   inte=ProcesamientoEntidadesIntents.get_json(
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[0],
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[1]),
                                   chat=chat, intent=intent[0],
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (MODIFICACION DE INFORMACION)
    # SET DATOS DEL AGENTE
    @app.route('/agente/editar/<string:chat>')
    def editar_agente(chat):
        if 'email' in session:
            return render_template("principal/modificar-datos/agente.html",
                                   agente=ProcesamientoAgente.get_agente('./usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # SET DATOS DEL ENTIDAD
    @app.route('/entidades/<string:chat>/entidad/editar/<string:entidad>')
    def editar_entidad(chat, entidad):
        if 'email' in session:
            entidad = ProcesamientoArchivos.relistado(entidad)
            return render_template("principal/modificar-datos/entidad.html",
                                   ent=ProcesamientoEntidadesIntents.get_json(
                                       './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[0],
                                       './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[1]),
                                   chat=chat, entidad=entidad[0],
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # SET DATOS DEL INTENT
    @app.route('/intents/<string:chat>/intent/editar/<string:intent>')
    def editar_intent(chat, intent):
        if 'email' in session:
            # intent = ProcesamientoArchivos.relistado(intent)
            return render_template("principal/modificar-datos/intent.html",
                                   inte=ProcesamientoEntidadesIntents.get_json(
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[0],
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[1]),
                                   chat=chat, intent=intent[0],
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ACTUALIZAR EL JSON DEL AGENTE
    @app.route('/actualizar_json', methods=["POST"])
    def actualizar_json():
        if 'email' in session:
            chat = request.args.get('chat')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            ProcesamientoAgente.set_agente('./usuarios/' + session['email'] + '/' + chat, clave, atributo)
            return redirect(url_for('get_agente', chat=chat))
        else:
            return redirect(url_for('login'))

    # ACTUALIZAR EL JSON DE LAS ENTIDADES
    @app.route('/actualizar_json_ent', methods=["POST"])
    def actualizar_json_ent():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            ProcesamientoEntidadesIntents.set_json(
                './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[0],
                './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad[1], clave, atributo)
            return redirect(url_for('get_entidad', chat=chat, entidad=entidad))
        else:
            return redirect(url_for('login'))

    # ACTUALIZAR EL JSON DE LOS INTENTS
    @app.route('/actualizar_json_int', methods=["POST"])
    def actualizar_json_int():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            ProcesamientoEntidadesIntents.set_json(
                './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[0],
                './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[1], clave, atributo)
            return redirect(url_for('get_intent', chat=chat, intent=intent))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------

    # página login
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            if ProcesamientoUsuario.verificar_usuario(email, password):
                rootdir = ProcesamientoUsuario.verificar_usuario(email, password)
                session['email'] = email

                if rootdir == './usuarios/':
                    return redirect(url_for('paginaprincipaladmin'))

                return redirect(url_for('paginaprincipal'))
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
        if 'email' in session:
            session.pop('email', None)
            return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------

    return app
