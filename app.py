from flask import Flask, render_template

app = Flask(__name__)


#pagina inicial de la pagina
@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


#pagina de inicio
@app.route('/login', methods=["GET"])
def login():
    return render_template("session/login.html")


#pagina de inicio
@app.route('/registro', methods=["GET"])
def registro():
    return render_template("session/registro.html")


#pagina principal
@app.route('/paginaprincipal', methods=["GET"])
def paginaprincipal():
    return render_template("principal/inicio.html")


#pagina con la informacion de creacion
@app.route('/about', methods=["GET"])
def about():
    return render_template("principal/about.html")


if __name__ == '__main__':
    app.run()
