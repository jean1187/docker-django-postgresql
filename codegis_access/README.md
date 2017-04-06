Instalación
===========

Requerimientos: Tener instalado python 3.5, PostgreSQL 9.6, PIP, virtualenv. 

Una vez clonado el repositorio, ingresar a la carpeta del proyecto para realizar los siguientes pasos:

Crear un virtualenv:
```
virtualenv -p python3.5 env --no-site-packages
```

Activar el virtualenv ( OSX / Linux ):
```
source env/bin/activate
```

(WINDOWS):
```
.\env\Scripts\activate.bat
```

Instalar los requerimientos de la aplicación:
```
(env) pip install -r requirements.txt
```

Sólo windows (instalar psycopg2) Descargar el binario desde el sitio web correspondiente a la versión de su SO:
```
32 bits (http://stickpeople.com/projects/python/win-psycopg/2.6.0/psycopg2-2.6.0.win32-py2.7-pg9.4.1-release.exe)

o

64 bits (http://stickpeople.com/projects/python/win-psycopg/2.6.0/psycopg2-2.6.0.win-amd64-py2.7-pg9.4.1-release.exe)
```

Luego instalarlo de la siguiente manera:
```
easy_install "C:\ubicacion\de\la\descarga-release.exe"
```

Instalar NodeJS y npm, luego instalar bower de forma global:
```
npm install -g bower
cd /static
bower install
cd ..
```

Copiar el archivo local_settings-dist.py para configurar la app con el equipo local, base de datos, email y otros:
```
cp codegis_access/local_settings-dist.py codegis_access/local_settings.py
```

Luego de editar los archivos copiados, sincronizar la base de datos y crear un super usuario:
```
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Montar servidor dev:
```
python manage.py runserver
```

Para salir del virtualenv:
```
deactivate
```