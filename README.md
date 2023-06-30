# ChatScriptor

<img href="https://chatscriptor.azurewebsites.net/" src="web/static/imagenes/CSLogoCompleto.png" alt="">

🔗 **Clica en el logo para acceder a la web**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-purple.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Índice

1. [¿Qué es ChatScriptor?] (#¿Qué-es-ChatScriptor?)
2. [Participantes] (#Participantes)
3. [Información relevante] (#Información-relevante)
4. [Licencia] (#Licencia)

## ¿Qué es ChatScriptor?

Dialogflow es una plataforma desarrollada por Google que permite desarrollar y administrar chatbots o asistentes
virtuales utilizando técnicas como el procesamiento del lenguaje natural (PNL) que facilitan las interacciones entre
aplicación y persona.

La interfaz que nos encontramos en su versión básica y gratuita está, actualmente, muy limitada.

Durante este proyecto, se analiza y evalúa esta herramienta, permitiendo identificar aquellos detalles que se han
considerado como necesidades actuales a la hora de crear un chatbot. Dada la relevancia de este tipo de productos, es
importante que posea elementos que hagan que la producción de chatbot esté al alcance de todos.

Es por esto, que este trabajo se propone desarrollar una interfaz gráfica que mejore la interacción con respecto a la
oficial de Google, así cómo añadir servicios que permitan optimizar y clarificar la experiencia del usuario.

ChatScriptor es la web resultante y se encuentra disponible en su página
oficial: https://chatscriptor.azurewebsites.net/

## Participantes

Trabajo de Fin de Grado en Ingeniería Informática bajo la Universidad de Burgos.

- Alumna: Claudia Landeira Viñuela
- Tutor: Raúl Marticorena Sánchez

### Información de contacto

Si se desea realizar alguna consulta o aportación: clv1003@alu.ubu.es

## Información relevante

### Estructura

- **/**: se trata del directorio raíz y en él se encuentran el archivo \textit{README}, la base de datos con los
  usuarios
  con sus contraseñas cifradas, la web, el archivo de requerimientos y el archivo \textit{Dockerfile}, con su respectivo
  archivo \textit{yml}
- **/web/** se trata del módulo correspondiente a la aplicación web y es donde se encuentra la aplicación Flask y sus
  subdirectorios
- **/web/endpoints/**: se trata del módulo correspondiente al desarrollo de los procesamientos de la web
- **/web/endpoints/traductor**: se trata del módulo que contiene los procedimientos para el traductor
- **/web/static/imagenes/**: se trata del módulo correspondiente a las imágenes estáticas que se usan en la interfaz
- **/web/static/css/**: se trata del módulo correspondiente a los archivos de diseño estáticos que se usan en la
  interfaz
- **/web/static/js/**: se trata del módulo correspondiente a las animaciones \textit{javascript} que se usan en la
  interfaz
- **/web/templates/**: se trata del módulo correspondiente a las diferentes pantallas de la interfaz web. En él se
  encuentran las pantallas de carga, la de registro y la de inicio de sesión
- **/web/templates/comunes/**: se trata del módulo que contiene las partes de la interfaz que son usadas en todas o la
  mayor
  parte de las pantallas
- **/web/templates/principal/**: se trata del módulo que contiene las pantallas de visualización y modificación de los
  chatbots, así como las pantallas de los buscadores
- **/docs/**: documentación del proyecto, en formato \textit{pdf} y \LaTeX, así como los archivos que contienen la
  información bibliográfica
- **/docs/img/**: imágenes utilizadas en la documentación
- **/img/**: imágenes relativas al directorio y al \textit{README} raíz
- **/usuarios/**: directorio donde se almacenan los chatbots de los usuarios

### Manual del programador

A continuación, se muestran los elementos usados para el desarrollo de este proyecto con el fin de permitir que, en caso
de continuar con el trabajo, cualquiera sea capaz de realizarlo con las mismas características con las que se ha
desarrollado.

#### Entorno de desarrollo

Los programas y dependencias usados para el desarrollo de este proyecto, han sido los siguientes:

- **Python 3.10**
- **PyCharm Professional**
- **Git**
- **Bibliotecas Python**: flask, bcrypt, transformers, torch, torchvision, sentencepiece, sacremose, waitress
- **Docker**

#### Instalación y ejecución del proyecto

Tal y como se ha descrito anteriormente, se deberán tener instalados todos los recursos nombrados. Para
facilitar este proceso, se ha incluido un archivo _Dockerfile_ que acelerará la configuración y ejecución.

##### Sin usar PyCharm

Este proyecto necesita diferentes dependencias y bibliotecas. Siguiendo los siguientes pasos se facilita la
configuración en cualquier máquina:

###### _**Paso 1: instalar Python**_

Es obligatorio y necesario tener instalado Python en tu máquina. Puedes descargarlo desde su sitio web
oficial: https://www.python.org/downloads/

La versión debe ser Python 3.10 en adelante.

###### _**Paso 2: clonación del repositorio**_

Clonar el repositorio alojado en GitHub:

~~~
git clone https://github.com/clv1003/Chat-Scriptor
cd Chat-Scriptor
~~~

###### _**Paso 3: Docker**_

La aplicación posee un archivo _Dockerfile_ que permite la ejecución e instalación de todos los requerimientos.
Para ellos, solo tendremos que construir la imagen y a continuación, iniciar el docker.

Introduciremos en la terminal el siguiente comando, deberán realizarse desde el directorio donde tengamos el proyecto:

~~~
docker compose up
~~~

Con esto, construiremos y ejecutaremos el contenedor docker a través de los archivos _Dokerfile_ y el
_docker-compose.yml_

Una vez finalice, si introducimos la dirección http://localhost:8080/ o http://127.0.0.1:8080/, podremos
acceder al servidor local con la aplicación.

Para terminar, podremos finalizar los procesos con el comando inverso:

~~~
docker compose down
~~~

##### Con PyCharm

Debido a que para el desarrollo del proyecto se ha usado este IDE, se añade la configuración exacta.

###### _**Paso 1: instalar Pycharm y Python**_

Para esta configuración, es necesario tener instalado el IDE Pycharm (en cualquiera de sus versiones, aunque si eres
alumno de la Universidad de Burgos podrás acceder a la versión Pycharm Professional)

La versión debe ser Python 3.10 en adelante. Puedes descargarlo desde su sitio web
oficial: https://www.python.org/downloads/

Para obtener Pycharm, puedes hacerlo desde su página oficial https://www.jetbrains.com/pycharm/download/?section=windows

###### _**Paso 2: clonación del repositorio**_

Clonar el repositorio alojado en GitHub:

~~~
git clone https://github.com/clv1003/Chat-Scriptor
cd Chat-Scriptor
~~~

###### _**Paso 3: abrir el proyecto en Pycharm**_

1. Abre PyCharm
2. Selecciona _Open_ en el menú inicial
3. Navega hasta la carpeta raíz del proyecto
4. Selecciona el archivo _pycharm.project_ o simplemente selecciona la carpeta raíz del proyecto

###### _**Paso 4: Docker**_

La aplicación posee un archivo \textit{Dockerfile} que permite la ejecución e instalación de todos los requerimientos.
Para ellos, solo tendremos que construir la imagen y a continuación, iniciar el docker.

Para ello, abriremos una terminal (_View -> Tool Windows -> Terminal_) y ejecutaremos el comando:

~~~
docker compose up
~~~

Con esto, construiremos y ejecutaremos el contenedor docker a través de los archivos _Dokerfile_ y el
_docker-compose.yml_

Una vez finalice, si introducimos la dirección http://localhost:8080/ o http://127.0.0.1:8080/, podremos
acceder al servidor local con la aplicación.

Para terminar, podremos finalizar los procesos con el comando inverso:

~~~
docker compose down
~~~

## Licencia

[The GNU General Public License](https://www.gnu.org/licenses/)
