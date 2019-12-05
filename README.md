# Manual de Instalación de DjangoLab V.2.3.1

_DjangoLab es un sistema de administración y difusión de investigación, orientada a centros de investigación, laboratorios y grupos de investigación_

## Ejemplos (examples) de los Web Sites con DjangoLab:

* [LascaWeb] (https://www.lasca.ic.unicamp.br/) - Desarrollado con DjangoLab 1.0
* [IIMAT-FCPN] (http://iimat.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.2
* [III-FCPN] (http://iii.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.2
* [IIF-FCPN] (http://iif.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.3.1
* [IBMB-FCPN] (http://ibmb.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.3.1
* [IE-FCPN] (http://ie.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.3.1
* [IETA-FCPN] (http://ieta.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.3.1
* [IIQ-FCPN] (http://iiq.fcpn.edu.bo/) - Desarrollado con DjangoLab 2.3.1

## Pre-requisitos 📋

_DjangoLab fue desarrollado sobre python 3.6 y Ubuntu 16.04. Los requerimientos mínimos son:_

* [Ubuntu 16.04 LTS o +/ Debian 8.0 o +] (https://ubuntu.com/about/release-cycle) - Sistemas Operativos usados en el proyecto, aunque soporta Windows.
* [Django 2.2 LTS] (https://www.djangoproject.com/download/) - Framework de desarrollo.
* [Python 3.6] (https://python3statement.org/) - Lenguaje de programación Python 3.6.8 (soporta desde Python 3.5 o +.

_Otros requerimientos técnicos mínimos:_

* Procesador: Intel Atom o Intel Core i3
* Disco de 10GB
* Memoria de 2GB (Para Ubunto o Debian)

Más información en: https://software.intel.com/en-us/distribution-for-python/system-requirements

## Instalación 🔧

##0. Comandos de ayuda:

_0.1. Versión de linux instalada._

```
	$ lsb_release -a
	OR
	$ cat /etc/os-release
```

_0.2. Verificar tamaño de disco:_
```
	$ df -h
```

_0.3. Actualizar el Sistema Operativo:_
```
	Para ubuntu:
	# apt-get update
	# apt-get upgrade
	Para Debian:
	# sudo apt-get update
    # sudo apt-get -y upgrade
```
_0.4. Dependencias básicas:_
Para Debian usar:
https://pythonchile.cl/post/2018/02/07/python3-en-debian-8-y-9/
```
	$ sudo apt install python3.6 // Python 3.5 o +
	$ python3 --version
		> Python 3.6.8
	$ sudo apt install python3-pip
	$ pip3 --version
		> pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```	
Para Debian:
```
	$ sudo pip3 install --upgrade setuptools

	$ pip3 install Pillow
	Pillow es una libreria para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes. 
```

_1. Configuración de virtalenv:_

_1.1. Instalar dependencias necesarias:_
```
	$ sudo apt-get install apache2 libapache2-mod-wsgi-py3
	
	Para Debian:
	$ sudo apt-get install apache2
	$ sudo apt-get install libapache2-mod-wsgi-py3
```

_1.2 Configuración de Python Virtual Environment:_
```
	$ pip3 install virtualenv
		> Successfully installed virtualenv-16.6.2
	
	# Para Debian instalar:
	$ sudo apt install python3-venv
	
	$ Verificar la posición de instalación:
	$ pwd
		> home/user
	Crear la carpeta de trabajo
	$ mkdir djangolab
	$ cd djangolab
	Dentro de la carpera django, crear el ambiente virtual Python:
	$ virtualenv djangolabenv
		> done.
		
	# Para Debian:
	$ python3 -m venv djangolabenv
	
	#IMPORTANTE# Caso de ERRORES con venv usar este manual: https://vitux.com/install-python3-on-ubuntu-and-set-up-a-virtual-programming-environment/
	$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
	$ pip3 -V
	$ sudo apt-get update
	$ sudo apt install python3-pip
	$ pip3 install virtualenv
	$ sudo apt install -y python3-venv
	$ python3 -m venv djangolabenv
	
	$ Activar el entorno virtual desde la misma posición:
	$ source ~/djangolab/djangolabenv/bin/activate
		> (djangolabenv) user@server:~/djangolab$
```

_2. Instalar Django y configuación en el Entorno Virtual (no salir):_

	Link de versiones: https://www.djangoproject.com/download/
```
	Instalar los siguientes paquetes:
	$ sudo apt install python3.6
	Instalar una version LTS de Django 2.2, se recomienda revisar la última version de Django 2.2 en https://www.djangoproject.com/download/
	$ pip3 install django==2.2.8 
	Verificar la version de Django instalada
	$ python3 -m django --version
		> 2.2.8 o superior
	OR
	$ python3
	>>> import django
	>>> django.VERSION
	(2, 2, 8, 'final', 0)
```
_2.1.  Instalar otros programas necesarios_
```
	$ sudo apt install python-django
	$ sudo apt install python-django-common
```

_2.2. Revisa todas las versiones de paquetes python instalados_
```
	$ pip3 freeze
		Django==2.2.8
		pytz==2019.3
		sqlparse==0.3.0

	Validar la versión de django-admin instalado
	$ django-admin --version
	> 2.2.8
```
_2.3. Verificar los paquetes instalados por django-admin_
```
	$ django-admin
	[django]
		check
		compilemessages
		createcachetable
		...
```
_3. Instalar PostgresSQL y configuración dentro del entorno virtual (no salir):_

Links: 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html
```
	Adicionar estos pasos para Debian:
	$ wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
	sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
```
_3.1. Instalar PostgreSQL y sus dependencias_
```
	$ sudo apt-get install postgresql postgresql-contrib
```

_3.2. Instalar dependencias de PostgreSQL para Django psycopg2_
```
	$ sudo apt-get install postgresql-client postgresql-client-common
	$ sudo apt install libpq-dev python-dev
	$ pip3 install psycopg2
```

_3.3. Acceder al Prompt de Postgres y cambiar la contraseña:_
```
	$ sudo -u postgres psql
	# \l 	retornará la lista de bases de datos en postgres
	Cambiamos la contraseña
	# \password postgres 	# new password: xxxxxxxx
	# \q 	salir de postgres
```

_3.4. Creamos la base de datos labdb:_
```
	$ sudo -u postgres createdb labdb
	OR
	$ sudo -u postgres psql
	# create database labdb
	# \l	Y vemos la BD labdb
	# \q
```

_4. Creación y configuración del proyecto djangolab, y app academic desde el entorno virtual (no salir)._

_4.1. Creación y primera ejecución_
```
	(djangolabenv) $ django-admin.py startproject djangolab ~/djangolab

	Configurar settings.py
	$ nano djangolab/settings.py
	Modificar:
		ALLOWED_HOSTS = ['*']
	Salvar
```

_Verifica si el proyecto se está ejecutando correctaente:_
```
	$ python3 manage.py runserver 0:8080
	$ python3 manage.py runserver 0:8000
```

_4.2. Creación de la app academic_
```
	$ python3 manage.py startapp academic
```

_4.3. Copiar los siguientes archivos:_
```
	academic/admin.py
	academic/forms.py
	academic/models.py
	academic/tests.py
	academic/urls.py
	academic/views.py
	djangolab/settings.py
	djangolab/urls.py
	media/*
	static/*
	templates/*
```

_4.4. Reemplazar los siguientes archivos por tus imágenes:_
```
	media/images/logo.png			<-- logo del institutos en formato png
	media/images/no-img.png			<-- logo del institutos en formato png
	static/academic/img/logo.ico	<-- logo del institutos en formato ico
	static/academic/img/logo.png	<-- logo del institutos en formato png
	static/academic/img/logocarrera.png<-- logo del institutos en formato png
```

_5. Instalación y Configuración de Django Publications desde el entorno virtual (no salir):_

Link: https://github.com/lucastheis/django-publications

5.1. Instalando & configurando Django Publications
```
	$ pip3 install django-publications
		> Successfully installed Pillow-6.2.1 django-publications-1.0.0
```
_5.2. Reemplazar los siguientes archivos a los siguientes posiciones de publications a djangolabenv/lib/python3.6/site-packages/publications/_
```
	templates/base.html
	templates/publications/publications.html
	templates/publications/publication.html
```

_5.3. Verificar errores:_
```
	$ python3 manage.py check
		> System check identified no issues (0 silenced).
```

_6. Completar la configuración inicial del proyecto desde el entorno virtual (no salir):_
```
6.1. Migración de la base de datos:
	$ python3 manage.py makemigrations
	$ python3 manage.py migrate
```

_6.2. Creamos un superusuario para el administrador:_
```
	$ python3 manage.py createsuperuser
	> user: nombre_usuario
	> email: email@usuario.com
	> password: xxxxxxxx
```

_6.3. Ingresar a settings y habilitar la opción para collectstatic_
```
	$ nano djangolab/settings.py
	Linea 136 adicionar comentarios ''':

'''	
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]
'''

AND en la línea 134 quitar comentario (#):

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

_6.4. Recolectar archivos estáticos en /static/_0
```
	$ python3 manage.py collectstatic
		> yes
		> 121 static files copied to '/home/marcelo/djangolab/static'.
	Podrá observar que se creo nuevas carpetas y archivos en static
```

_6.5. Ingresar a settings a la opción por defecto_
```
	$ nano djangolab/settings.py
	Linea 136 quitar comentarios:

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

AND en la línea 134 adicionar comentario (#):

#STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

_6.6. Configurar el UFW firewal para la puerta 8000 o 8080:_

_6.6.1. Verificar estado del Firewall_
```
	$ sudo ufw status
```

_6.6.2. (OPCIONAL) En caso de activar el Firewall, ejecutar los siguientes comandos con cuidado:_
```
	(OPCIONAL) $ sudo ufw default deny
	$ sudo ufw enable
	$ sudo ufw allow 8000
	$ sudo ufw allow 2223
	$ sudo ufw allow ssh
	$ sudo ufw allow 'Apache Full'
	(OPCIONAL) $ sudo ufw allow 8800
		Rules updated
		Rules updated (v6)
	$ sudo ufw status
	(OPCIONAL) $ sudo ufw disable
	(OPCIONAL) $ sudo ufw reset ==> Resetear con la configuración inicial.
```
Link 1: https://linuxize.com/post/how-to-setup-a-firewall-with-ufw-on-ubuntu-18-04/
Link 2: https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-16-04
```
	$ sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
```

_7. Iniciar servicio de DjangoLab V2.3.1_
```
	$ python3 manage.py runserver 0:8080
	$ python3 manage.py runserver 0:8000
```

_7.1. Ingresar al 127.0.0.1:8000/admin y acceder con las credenciales creadas en 6.2:_
```
	Ingresar a Academic > D. Cargos/Puestos del Instituto y añadir los siguientes puestas en este orden:
		1) Director(a)
		2) Coordinador(a)
		3) Docente Investigador
		4) Auxiliar de Investigación
		5) Estudiante Investigador Junior
		5) Investigador Asociado
		6) Personal Administrativo
	* RESPETA EL ORDEN, PUES INFLUENCIARÁ EN LA SECCIÓN DE PERSONAL Y REPORTES
```

_7.2. Optimización de Postgres:_
```
	$ sudo -u postgres psql
	postgres=# ALTER ROLE postgres SET client_encoding TO 'utf8';
		> ALTER ROLE
	postgres=# ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
		> ALTER ROLE
	postgres=# ALTER ROLE postgres SET timezone TO 'UTC';
		> ALTER ROLE
	postgres=# \q
```

_8. Configuración de Apache Server por mod_wsgi:_

_ Concluido con la configuración, el sistema estará funcionando correctamente. Desactivamos el entorno virtual:_
```
	(djangolabenv) $ deactivate
```
_8.1. Configurar WSGI. Editar el archivo de host virtual predeterminado:_0
```
	$ sudo nano /etc/apache2/sites-available/000-default.conf

=============================  000-default.conf ==========================

<VirtualHost *:80>

        ServerAdmin marcelopalma@fcpn.edu.bo
        DocumentRoot /var/www/html

        LogLevel     warn
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static/ /home/marcelo/djangolab/static/
        <Directory /home/marcelo/djangolab/static>
                Require all granted
        </Directory>

        Alias /media/ /home/marcelo/djangolab/media/
        <Directory /home/marcelo/djangolab/media>
                Require all granted
        </Directory>


        # Next, add the following directory block
        <Directory /home/marcelo/djangolab/djangolab>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess djangolab python-home=/home/marcelo/djangolab/djangolabenv python-path=/home/marcelo/djangolab/
        WSGIProcessGroup djangolab
        WSGIScriptAlias / /home/marcelo/djangolab/djangolab/wsgi.py

</VirtualHost>

===========================================================================
```

_En caso de error:_
```
Error: Django [Errno 13] Permission denied: '/var/www/media/animals/user_uploads'
https://stackoverflow.com/questions/21797372/django-errno-13-permission-denied-var-www-media-animals-user-uploads
```

_8.2. (NO RECOMENDADO) Dar permisos a www-data para acceder a djangolab:_
```
	$ chmod 775 ~/djangolab
	$ sudo chown :www-data ~/djangolab
```

_8.3. (OPCIONAL) Configuración adicional del Firewall:_
```
	$ sudo ufw delete allow 8000
	$ sudo ufw allow 'Apache Full'
	$ sudo iptables -D INPUT -p tcp --dport 8000 -j ACCEPT
	$ sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
```

_8.4. Verificación de configuración Apache2:_
```
	$ sudo apache2ctl configtest
		> Syntax OK

	# Caso exista un error (Debian):
	$ sudo a2enmod wsgi
	$ sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

_8.5. Puesta en marcha del servidor:_
```
	$ sudo systemctl restart apache2
```

## Auxiliares:
_Trabajar con el shell del proyecto djangolab: ⚙️_
```
	$ python3 manage.py shell
	>>> import django
	>>> from academic.models import *
```
_Trabajar con el dbshell del proyecto djangolab para revisar la base de datos del proyecto y su contenido._

## Agradecimientos:

_Agradezco a @lucastheis por el desarrollo de Django Publications 1.0.0, el cual contribuyo al desarrollo de este DjangoLab_

Link: https://github.com/lucastheis/django-publications
Link: https://pypi.org/project/django-publications/