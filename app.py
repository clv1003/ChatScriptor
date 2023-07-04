from web import start_app

'''
app.py
@Author: Claudia Landeira

Llamada al __init__ que inicializa la aplicación Flask
'''

app = start_app()

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

