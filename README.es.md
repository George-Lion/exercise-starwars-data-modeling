# Diagrama de base de datos Star Wars

Aplicando la relación entre `Primary_key` y `ForeignKey` se pueden conectar cada una de las tablas con las que se desea recibir o enviar
información, para realizar el diagrama de star wars se utilizó `quick data base diagrams`, la base de datos cuenta con varias tablas divididas en 
`user`,`favorites`,`characters`, `planets`,`vehicles`. La finalidad poder almacenar a nuestra tabla de favoritos la información que se encuentra en
las otras tablas.

<img src="/img/diagram.jpg" alt="diagram"/>

-----------------------------------------------------------------------------

# StarWars blog database (base de datos)

**Importante**: Para realizar esta actividad necesitas hacer un `fork` de este repo en tu cuenta de **Github** y luego, abrir el *fork* en Gitpod.

Dentro del archivo `src/models.py` encontrarás un par de clases que describen una base de datos de ejemplo.

Aquí hay un video de 4 minutos que explica qué es UML: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

Vamos a crear el Diagrama de relación de entidad para la base de datos de un blog de StarWars, un diagrama muy similar a este:

![Diagrama de Starwars](https://github.com/breatheco-de/exercise-starwars-data-modeling/blob/master/assets/example.png?raw=true)
[Clic para abrir el diagrama](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 Puedes usar esta herramienta GRATUITA para practicar tu diagrama por primera vez: https://app.quickdatabasediagrams.com/#/d/

## 💻 Instalación

1. Entra dentro del environment (ambiente) `$ pipenv shell`

2. Instala todas las dependencias `$ pipenv install`

3. Genera el diagrama tantas veces como sea necesario `$ python src/models.py`

4. Abre el archivo `diagram.png` para ver tu diagrama UML!


## 📝Instrucciones

Tu trabajo es actualizar el archivo `src/models.py` con el código necesario para replicar el modelo de datos de un blog de StarWars.

El proyecto está utilizando la librería Python SQLAlchemy para generar la base de datos.

- Tu proyecto debe tener una tabla `Usuario` que va a contener la información de cada uno de tus usuarios.
- Los usuarios del blog podrán iniciar sesión y guardar sus planetas o personajes favoritos.
- Tu base de datos debe guardar los favoritos de cada usuario del blog para su posterior revisión.
- Tu base de datos también debe almacenar cada planeta y personaje de starwars.
- ¿Qué otras tablas crees que necesitarás para tu aplicación?
- ¿Qué propiedades deben ir dentro de cada tabla? Por ejemplo: El usuario tiene email, password, fecha de subscripción, nombre, apellido, etc.
- ¿Qué relaciones hay entre las tablas? ¿Cuántos planetas puede guardar un usuario?
   
Nota: Recuerda que las relaciones pueden ser Uno-a-uno, Uno-a-muchos o Muchos-a-muchos.

- Porfavor agrega por lo menos 4 modelos y sus respectivas relaciones.
- General el `diagrama.png` utilizando el comando `$ python3 models.py` en la consola.
