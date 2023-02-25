# Django

- Django es un framework de aplicaciones web utlizando python, django te permite crear aplicaciones web de forma rapidas simplificandote la mayor cantidad de tarea repetitivas este framwerok te permite utlizar

1. `database`
2. `Auth`
3. `Form`
4. `protected route`
5. `ADMIN PANEL`

## virtual environment

- Un entorno virtual no es mas que una forma de separar modulos en diferentes proyectos

[![Entorno Virtual](https://i.postimg.cc/0ybL5w2Y/Captura-de-pantalla-2023-02-23-225531.png)](https://postimg.cc/87gytsvc)

## instalacion de Django

1. `Crea un entorno virtual` En mi caso estarre usando pipenv

2. `Ejecuta el siguiente comando`

```
pipenv install django
```

3. `Si estas usando pip`

```
pip install django
```

4. `Comprueba si django se ha instalado correctamente.`

```
django-admin --version
```

5. `version` En mi caso me ha dado la version **4.1.7**

## Crea un proyecto en django

- Sigue los siguientes paso y crearas un proyecto en django

### Primera forma

1. `Ejecuta el siguiente comando en la terminal`

```
django-admin startproject <name-project>
```

- Esto creara un proyecto de django en tu carpeta.

### Segundo forma

2. `Ejecuta el siguiente comando en la terminal`

```
django-admin startproject <name-project> .
```

- Ahora si tu no quieres que tu proyecto este en un directorio dentro de otro directorio este comando no va a crear el primer directorio... tan solo el proyecto

## Archivo manage.py

- el archivo `manage.py` nos permite ejecutar comando de administracion que nos ayudaran en nuestro proyecto como por ejemplo un

1. `servidor de desarrollo`
2. `Copiar archivos`
3. `Optimizar nuestra aplicacion`

### ejecuta tu servidor web

- SI nosotros vamos a ejecutar nuestra servidor web, vamos a escribir el siguiente comando en la consola

```
python manage.py runserver
```

- esto te va abrir un mensaje por consola que dice:
  `Starting development server at ` y puede salirte algunas de las siguientes opciones:

1. [`127.0.0.1:8000`](http://`127.0.0.1:8000)
2. [`localhost:8000`](`localhost:8000)

- si le has dado click algunas de las siguientes funciones debe salirte esta interfaz

[![Captura-de-pantalla-2023-02-23-232849.png](https://i.postimg.cc/JnpdNrp3/Captura-de-pantalla-2023-02-23-232849.png)](https://postimg.cc/LYZTRpKh)

**_FELICITACIONES HAS CREADO UN PROYECTO EN DJANGO_**

## estrutura del proyecto

- hasta ahora la estrutura de nuestro proyecto debe ser la siguiente

1. `<nombre de nuestro directorio>` codigo fuente de nuestra aplicacion en mi caso es ***learningDjango**

2. `db.sqlite` cuando ejecutamos nuestro proyecto ha parecido este archivo , lo cual es la base de datos que usa django por defecto

3. `manage.py` este archivos es el de administracion

## comando extras

```
python manage.py --help
```

### ***output***: 
```
Available subcommands:

[auth]
    changepassword
    createsuperuser --crear usuario para administrador

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages --copilar mensajes
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver --obtener un servidor de testing
```

* esta es la salida que hemos tenido con aquel comando estos son comando que ya estan definiodo por django para darle uso nosotros podemos darle uso cada uno hace algo diferente esta en ti probarlos



## probando la carpeta ***learningDjango***

* si entramos a esta carpeta los primeros que podemos observar son los siguientes archivos: 

1. ***init.py*** : este archivo es para decirle a python que este directrio es un modulo de nuestro proyecto

2. ***setting.py**: este archivo es para que nosotros podeamos configurar nuestro proyecto

3. ***urls.py**: este archivo tiene las rutas que el usuario puede visitar

3. ***asgi.py and wsgi.py** : estos dos archivos sirven el contenido 