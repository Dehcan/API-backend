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

Templates y archivos estaticos, configuracion
1. Configurar Template en "settings.py"
    import os

    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]
2. Configurar archivos estaticos y media en "settings.py"
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  
3. Crear la estructura
    templates/
    media/
    static/
        css/
        js/
        images/
4. Crear archivo templates/base.html
    <!-- <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>{% block title %}Medios de Arte{% endblock %}</title>
    {% load static %} -->
    <!-- CSS de Bootstrap desde CDN -->
    <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"> -->
    <!-- Tu archivo de estilos CSS -->
    <!-- <link rel="stylesheet" href="{% static 'css/estilos.css' %}">
    </head>
    <body> -->
    <!-- Barra de navegación -->
    <!-- <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'usuarios:login' %}">Medios de Arte</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContenido" aria-controls="navbarContenido" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContenido">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'libros:lista_articulos' %}">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'peliculas:lista_cartel' %}">Galería</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                {{ user.username }}
                            </a>
                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                                {% if user.perfil.rol == 'administrador' %}
                                    <a class="dropdown-item" href="{% url 'admin:index' %}">Panel de Administración</a>
                                {% endif %}
                                <a class="dropdown-item" href="#">Perfil</a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="{% url 'usuarios:logout' %}">Cerrar Sesión</a>
                            </div>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'usuarios:login' %}">Iniciar Sesión</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'usuarios:registro' %}">Registrarse</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav> -->

    <!-- Contenido principal -->
    <!-- <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div> -->

    <!-- Pie de página -->
    <!-- <footer class="bg-dark text-white mt-4">
        <div class="container text-center py-3">
            &copy; 2024 Alejandro Merino. Todos los derechos reservados.
        </div>
    </footer> -->

    <!-- JavaScript de Bootstrap desde CDN -->
    <!-- <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script
        src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js">
    </script>
    <script
        src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js">
    </script> -->
    <!-- Tu archivo de scripts JS -->
    <!-- <script src="{% static 'js/scripts.js' %}"></script>
    </body>
    </html>  -->

