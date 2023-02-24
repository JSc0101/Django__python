# Django

* Django es un framework de aplicaciones web utlizando python, django te permite crear aplicaciones web de forma rapidas simplificandote la mayor cantidad de tarea repetitivas este framwerok te permite utlizar 

1. `database` 
2. `Auth`
3. `Form`
4. `protected route`
5. `ADMIN PANEL`


## virtual environment

* Un entorno virtual no es mas que una forma de separar modulos en diferentes proyectos

[![Entorno Virtual](https://i.postimg.cc/0ybL5w2Y/Captura-de-pantalla-2023-02-23-225531.png)](https://postimg.cc/87gytsvc)


## instalacion de Django

1. `Crea un entorno virtual` En mi caso estarre usando pipenv

2. `Ejecuta el siguiente comando` 

```
pipenv install django
```

3. `Si estas usando pip`

````
pip install django
````

4. `Comprueba si django se ha instalado correctamente.`

````
django --version
````

5. `version` En mi caso me ha dado la version **4.1.7**


## Crea un proyecto en django

* Sigue los siguientes paso y crearas un proyecto en django

### Primera forma

1. `Ejecuta el siguiente comando en la terminal`
````
django-admin startproject <name-project>
````

* Esto creara un proyecto de django en tu carpeta.

### Segundo forma

2. `Ejecuta el siguiente comando en la terminal`
`````
django-admin startproject <name-project> .
`````

* Ahora si tu no quieres que tu proyecto este en una carpeta dentro de otra carpeta este comando no va a crear la primera carpeta tan solo el proyecto


## Archivo manage.py

* el archivo `manage.py` nos permite ejecutar comando ed administracion que nos ayudaran en nuestro proyecto como por ejemplo un 

1. `servidor de desarrollo`
2. `Copiar archivos`
3. `Optimizar nuestra aplicacion`

### ejecuta tu servidor web

* SI no nosotros vamos a ejecutar nuestra servidor web, vamos a escribir el siguiente comando en la consola

````
python manage.py runserver
````

* esto te va abrir un mensaje por consola que dice:
`Starting development server at ` y puede salirte algunas de las siguientes opciones:

1. [`127.0.0.1:8000`](http://`127.0.0.1:8000)
2. [`localhost:8000`](`localhost:8000)

* si le has dado click algunas de las siguientes funciones debe salirte esta interfaz

[![Captura-de-pantalla-2023-02-23-232849.png](https://i.postimg.cc/JnpdNrp3/Captura-de-pantalla-2023-02-23-232849.png)](https://postimg.cc/LYZTRpKh)

***FELICITACIONES HAS CREADO UN PROYECTO EN DJANGO***