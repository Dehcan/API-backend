[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Nyz_m2tV)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17078082)

Configuracion inicial del proyecto:
1. crear entorno virtual(en VSC) 
    python -m venv .venv
2. instalar Django
    pip install django
3. crear proyecto Django
    django-admin startproject nombre_proyecto
4. instalar Pillow
    pip install pillow
5. instalar Cryptography
    pip install cryptography

Crear Aplicaciones:
1. Crear App Usuarios
    python manage.py startapp usuarios
2. Crear App Libros
    python manage.py startapp libros
3. Crear App Peliculas
    python manage.py startapp peliculas

Configurar apropiadamente "settings.py"
1. Añadir a "INSTALLED_APPS" las aplicaciones respectivas dentro de "settings.py"
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Nuevas Aplicaciones
    'usuarios',
    'libros',
    'peliculas',
]
2. Establecer Zona Horaria y Configurar el Idioma en "settings.py"
    LANGUAGE_CODE = 'es-es'
    TIME_ZONE = 'America/Santiago'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
3. Instalar conector Python para MySQL
    pip install pymysql
4. Instalar paquete para variables de entorno
    pip install python-decouple
5. Crear archivo .env en la raiz para las credenciales DB
    DB_NAME=nombre_bd
    DB_USER=nombre_usuario
    DB_PASSWORD=contraseña
6. Crear archivo .gitignore
    *.pyc
    *.sqlite3
    .env/
    .DS_Store
    .env
7. Actualizar datos de DB en "settings.py"
    from decouple import config
    import pymysql
    pymysql.install_as_MySQLdb()
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
    }

