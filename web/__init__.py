import os
from asyncio import ProactorEventLoop

from flask import Flask, render_template, url_for, redirect, request, session

import ProcesamientoAgente
import ProcesamientoArchivos
import ProcesamientoEntidadesIntents
import ProcesamientoZip
import ProcesamientoUsuario
import ProcesamientoBuscador


def start_app():
    app = Flask(__name__, static_folder='static')
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
    @app.route('/home', methods=["GET"])
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

    # pagina principal del administrador
    @app.route('/admin', methods=["GET"])
    def paginaprincipaladmin():
        if 'email' in session:
            if os.path.exists('./usuarios'):
                return render_template("principal/admin.html",
                                       datos=ProcesamientoArchivos.get_disponible('./usuarios'),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/admin/remove', methods=["POST"])
    def removeuser():
        if 'email' in session:
            chat = request.args.get('chat')
            if os.path.exists('./usuarios/' + chat):
                ProcesamientoUsuario.remove_user(chat)
                return redirect(url_for('paginaprincipaladmin'))
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

    @app.route('/menu/<string:chat>', methods=["GET"])
    def get_archivos(chat):
        if 'email' in session:
            return render_template('principal/pantallas/menu.html',
                                   arbol=ProcesamientoArchivos.get_arbol('./usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # GET DATOS DEL AGENTE
    @app.route('/agente/<string:chat>', methods=["GET"])
    def get_agente(chat):
        if 'email' in session:
            return render_template("principal/pantallas/agente.html",
                                   agente=ProcesamientoAgente.get_agente('./usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # GET DATOS DEL ENTIDADES
    @app.route('/entidades/<string:chat>', methods=["GET"])
    def get_entidades(chat):
        if 'email' in session:
            return render_template("principal/pantallas/entidades.html",
                                   entidades=ProcesamientoEntidadesIntents.get_entidades(
                                       './usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/entidades/<string:chat>/entidad/<string:entidad>', methods=["GET"])
    def get_entidad(chat, entidad):
        if 'email' in session:
            entidad = ProcesamientoArchivos.relistado(entidad)
            return render_template("principal/pantallas/entidad.html",
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
            return render_template("principal/pantallas/intents.html",
                                   intents=ProcesamientoEntidadesIntents.get_intents(
                                       './usuarios/' + session['email'] + '/' + chat),
                                   chat=chat, usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/intents/<string:chat>/intent/<string:intent>', methods=["GET"])
    def get_intent(chat, intent):
        if 'email' in session:
            intent = ProcesamientoArchivos.relistado(intent)
            return render_template("principal/pantallas/intent.html",
                                   inte=ProcesamientoEntidadesIntents.get_json(
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[0],
                                       './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent[1]),
                                   chat=chat, intent=intent[0],
                                   usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (MODIFICACION DE INFORMACION)
    # ACTUALIZAR EL JSON DEL AGENTE
    @app.route('/actualizar_json', methods=["POST"])
    def actualizar_json():
        if 'email' in session:
            chat = request.args.get('chat')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            ProcesamientoAgente.set_agente('./usuarios/' + session['email'] + '/', chat, clave, atributo)
            return redirect(url_for('get_agente', chat=chat))
        else:
            return redirect(url_for('login'))

    # =======================================================================
    # ACTUALIZAR EL JSON DE LAS ENTIDADES
    @app.route('/actualizar_json_ent', methods=["POST"])
    def actualizar_json_ent():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                if clave == 'name':
                    ProcesamientoEntidadesIntents.editar_nombre(
                        './usuarios/' + session['email'] + '/' + chat + '/entities/' + entidad,
                        clave=clave, atributo=atributo)
                    return redirect(url_for('get_entidades', chat=chat))
        else:
            return redirect(url_for('login'))

    @app.route('/actualizar_v_ent', methods=["POST"])
    def actualizar_v_ent():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            value = request.args.get('value')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.editar_v_ent(
                    './usuarios/' + session['email'] + '/' + chat,
                    value=value, entidad=entidad, atributo=atributo)
                return redirect(url_for('get_entidades', chat=chat))

        else:
            return redirect(url_for('login'))

    @app.route('/actualizar_s_ent', methods=["POST"])
    def actualizar_s_ent():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            value = request.args.get('value')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.editar_s_ent(
                    './usuarios/' + session['email'] + '/' + chat,
                    value=value, entidad=entidad, atributo=atributo)
                return redirect(url_for('get_entidades', chat=chat))

        else:
            return redirect(url_for('login'))

    # =======================================================================
    # ACTUALIZAR EL JSON DE LOS INTENTS
    @app.route('/actualizar_json_int', methods=["POST"])
    def actualizar_json_int():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            clave = request.args.get('clave')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                if clave == 'name':
                    ProcesamientoEntidadesIntents.editar_nombre(
                        './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent,
                        clave=clave, atributo=atributo)
                    return redirect(url_for('get_intents', chat=chat))
        else:
            return redirect(url_for('login'))

    @app.route('/actualizar_responses', methods=["POST"])
    def actualizar_responses():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            subclave = request.args.get('subclave')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.editar_responses(
                    './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent,
                    subclave=subclave, atributo=atributo)
                return redirect(url_for('get_intents', chat=chat))

        else:
            return redirect(url_for('login'))

    @app.route('/actualizar_data', methods=["POST"])
    def actualizar_data():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            old = request.args.get('old')
            tipo = request.args.get('tipo')
            atributo = request.form['atributo']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.editar_data(
                    './usuarios/' + session['email'] + '/' + chat,
                    intent=intent, old=old, tipo=tipo, atributo=atributo)
                return redirect(url_for('get_intents', chat=chat))

        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (AÑADIR)
    # AÑADIR ENTRY
    @app.route('/add_entry', methods=["POST"])
    def add_entry():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            value = request.form['value']
            synonyms = request.form['synonyms']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.add_entry(
                    './usuarios/' + session['email'] + '/' + chat,
                    entidad=entidad, value=value, synonyms=synonyms)
                return redirect(url_for('get_entidades', chat=chat))
        else:
            return redirect(url_for('login'))

    # AÑADIR RESPONSES
    @app.route('/add_responses', methods=["POST"])
    def add_responses():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            name = request.form['name']
            dataType = request.form['dataType']
            value = request.form['value']

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.add_responses(
                    './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent,
                    name=name, dataType=dataType, value=value)
                return redirect(url_for('get_intents', chat=chat))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    # TRATAMIENTO DE LOS DATOS DE LOS CHATBOTS (ELIMINAR)
    # ELIMINAR CHATBOT
    @app.route('/remove_chatbot', methods=["POST"])
    def remove_chatbot():
        if 'email' in session:
            chat = request.args.get('chat')
            if os.path.exists('./usuarios/' + session['email']):
                ProcesamientoArchivos.remove_chatbot('./usuarios/' + session['email'] + '/', chat)
                return redirect(url_for('paginaprincipal'))
            else:
                return redirect(url_for('paginaprincipal'))
        else:
            return redirect(url_for('login'))

    # ELIMINAR ENTIDAD
    @app.route('/remove_entidad', methods=["POST"])
    def remove_entidad():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')

            if os.path.exists('./usuarios/' + session['email']):
                ProcesamientoEntidadesIntents.remove_entidad('./usuarios/' + session['email'] + '/', chat, entidad)
                return redirect(url_for('get_entidades', chat=chat))
            else:
                return redirect(url_for('get_entidades', chat=chat))
        else:
            return redirect(url_for('login'))

    @app.route('/remove_entry', methods=["POST"])
    def remove_entry():
        if 'email' in session:
            chat = request.args.get('chat')
            entidad = request.args.get('entidad')
            value = request.args.get('value')
            synonyms = request.args.get('synonyms')

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.remove_entry(
                    './usuarios/' + session['email'] + '/' + chat,
                    entidad=entidad, value=value, synonyms=synonyms)
                return redirect(url_for('get_entidades', chat=chat))
        else:
            return redirect(url_for('login'))

    # ELIMINAR INTENT
    @app.route('/remove_intent', methods=["POST"])
    def remove_intent():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')

            if os.path.exists('./usuarios/' + session['email']):
                ProcesamientoEntidadesIntents.remove_intent('./usuarios/' + session['email'] + '/', chat, intent)
                return redirect(url_for('get_intents', chat=chat))
            else:
                return redirect(url_for('get_intents', chat=chat))
        else:
            return redirect(url_for('login'))

    @app.route('/remove_responses', methods=["POST"])
    def remove_responses():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            idR = request.args.get('id')

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.remove_responses(
                    './usuarios/' + session['email'] + '/' + chat + '/intents/' + intent, idR=idR)
                return redirect(url_for('get_intents', chat=chat))
        else:
            return redirect(url_for('login'))

    @app.route('/remove_data', methods=["POST"])
    def remove_data():
        if 'email' in session:
            chat = request.args.get('chat')
            intent = request.args.get('intent')
            idD = request.args.get('id')

            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                ProcesamientoEntidadesIntents.remove_data(
                    './usuarios/' + session['email'] + '/' + chat, intent=intent, idD=idD)
                return redirect(url_for('get_intents', chat=chat))
        else:
            return redirect(url_for('login'))

    # --------------------------------------------------------------------------------------------------------
    @app.route('/buscar_agente/<string:chat>', methods=["GET"])
    def buscar_agente(chat):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                return render_template("principal/buscador/buscadorAgente.html",
                                       resultados=ProcesamientoBuscador.buscar_agente(
                                           './usuarios/' + session['email'] + '/' + chat,
                                           busqueda=busqueda), chat=chat, busqueda=busqueda,
                                       agente=ProcesamientoAgente.get_agente(
                                           './usuarios/' + session['email'] + '/' + chat),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

        else:
            return redirect(url_for('login'))

    @app.route('/buscar_entidad/<string:chat>/<string:entidad>', methods=["GET"])
    def buscar_entidad(chat, entidad):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                enti = ProcesamientoEntidadesIntents.directoriosEntidad(
                    './usuarios/' + session['email'] + '/' + chat, entidad)
                return render_template("principal/buscador/buscadorEntidad.html",
                                       resultados=ProcesamientoBuscador.buscar_ent_int(enti[0], enti[1],
                                                                                       busqueda=busqueda),
                                       chat=chat, busqueda=busqueda, entidad=entidad,
                                       ent=ProcesamientoEntidadesIntents.get_json(enti[0], enti[1]),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

        else:
            return redirect(url_for('login'))

    @app.route('/buscar_intent/<string:chat>/<string:intent>', methods=["GET"])
    def buscar_intent(chat, intent):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                inten = ProcesamientoEntidadesIntents.directoriosIntent(
                    './usuarios/' + session['email'] + '/' + chat, intent)
                return render_template("principal/buscador/buscadorIntent.html",
                                       resultados=ProcesamientoBuscador.buscar_ent_int(inten[0], inten[1],
                                                                                       busqueda=busqueda),
                                       chat=chat, busqueda=busqueda, intent=intent,
                                       inte=ProcesamientoEntidadesIntents.get_json(inten[0], inten[1]),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))

        else:
            return redirect(url_for('login'))

    @app.route('/buscar_entidades/<string:chat>', methods=["GET"])
    def buscar_entidades(chat):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                return render_template("principal/buscador/buscadorEntidades.html",
                                       resultados=ProcesamientoBuscador.buscar_entidades(
                                           './usuarios/' + session['email'] + '/' + chat, busqueda=busqueda),
                                       chat=chat, busqueda=busqueda,
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/buscar_intents/<string:chat>', methods=["GET"])
    def buscar_intents(chat):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                return render_template("principal/buscador/buscardorIntents.html",
                                       resultados=ProcesamientoBuscador.buscar_intents(
                                           './usuarios/' + session['email'] + '/' + chat, busqueda=busqueda),
                                       chat=chat, busqueda=busqueda,
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/buscar_chatbot/<string:chat>', methods=["GET"])
    def buscar_chatbot(chat):
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                return render_template("principal/buscador/buscadorChatbot.html",
                                       resultados=ProcesamientoBuscador.buscar_chatbot(
                                           './usuarios/' + session['email'] + '/' + chat,
                                           busqueda=busqueda),
                                       chat=chat, busqueda=busqueda,
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    @app.route('/buscar_chatbots/', methods=["GET"])
    def buscar_chatbots():
        if 'email' in session:
            busqueda = request.args.get('busqueda')
            if os.path.exists('./usuarios/' + session['email']):
                return render_template("principal/buscador/buscadorChatbots.html",
                                       resultados=ProcesamientoBuscador.buscar_chatbots(
                                           './usuarios/' + session['email'], busqueda=busqueda), busqueda=busqueda,
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
        else:
            return redirect(url_for('login'))

    # ------------------------
    # REPORTE CON EL RESUMEN DE TODA LA INFORMACION RELEVANTE
    @app.route('/reporte/<string:chat>', methods=["GET"])
    def report(chat):
        if 'email' in session:
            intent = request.args.get('intent')
            if os.path.exists('./usuarios/' + session['email'] + '/' + chat):
                inten = ProcesamientoEntidadesIntents.directoriosIntent(
                    './usuarios/' + session['email'] + '/' + chat, intent)
                return render_template("principal/pantallas/reporte.html", chat=chat, intent=intent,
                                       inte=ProcesamientoEntidadesIntents.get_json(inten[0], inten[1]),
                                       usuario=ProcesamientoUsuario.get_usuario(email=session['email']))
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
