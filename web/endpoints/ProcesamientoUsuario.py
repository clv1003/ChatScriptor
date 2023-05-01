import csv
import os
import bcrypt


def registrar_usuario(nombre, email, password):
    # Verificar si el email ya está en uso
    with open('database.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if row[1] == email:
                return False

    # Encriptar la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Agregar el usuario al archivo CSV
    with open('database.csv', mode='a', newline='') as csv_file:
        fieldnames = ['nombre', 'email', 'password']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'nombre': nombre, 'email': email, 'password': hashed_password.decode('utf-8')})

    if os.path.exists('./usuarios/'):
        # Crear el directorio para el usuario
        os.mkdir('./usuarios/' + email)
    else:
        os.mkdir('./usuarios/')
        os.mkdir('./usuarios/' + email)

    return True


def verificar_usuario(email, password):
    with open('database.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if row[1] == email:
                if bcrypt.checkpw(password.encode('utf-8'), row[2].encode('utf-8')):
                    if administracion_usuarios(email):
                        return './usuarios/'
                    else:
                        return './usuarios/' + email
                else:
                    return False

    return False


def get_usuario(email):
    with open('database.csv', 'r') as db:
        reader = csv.reader(db, delimiter=';')

        for line in reader:
            if line[1] == email:
                return line[1]

    return None


def administracion_usuarios(email):
    correo = 'administrador@administrador.com'

    if email == correo:
        return True

    return False
