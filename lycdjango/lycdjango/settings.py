
import os
from pathlib import Path
import django.core.mail.backends.smtp

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-118lyoxk4kwqaa*g!pmakd8euo9nffxb%l2wcz$v6_(o@9)!jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    'registration.apps.RegistrationConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'productos',
    'contact',
    'politicas',
    'ckeditor',
    'pedidos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise
]

X_FRAME_OPTIONS = "SAMEORIGIN"
ROOT_URLCONF = 'lycdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.correo_empresa',
                'core.context_processors.copyright',# Agrega esta línea
            ],
        },
    },
]


WSGI_APPLICATION = 'lycdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# redireccionsr el login y logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# envio de emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'comercializadoralyc99@gmail.com'
EMAIL_HOST_PASSWORD = 'rzoc miwa gfnc jygq'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# STATIC FILES CONTENT CONFIG
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# ALMACEN DE ARCHIVOS QUE EL USUARIO SUBE, SON MODIFICABLES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ALMACEN DE ARCHIVOS ASSET ESTATICOS, NECESARIOS PARA IMLEMENTACION DEL SITIO
STATIC_URL = '/static/'
STATIC_TMP = os.path.join(BASE_DIR, 'core', 'static', 'core')
# DIRECTORIO DE DJANGO GENERADO AUTOMATICAMENTE, RECOPILA LOS ASSET DE LIBRERIAS PIP + TU RUTA DE STATIC
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# COMPRUEBA QUE LOS DIRECTORIOS EXISTAN
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)
# DIRECTORIOS STATICOS QUE DJANGO LEERA PARA LOS TEMPLATES
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core', 'static', 'core'),
    os.path.join(BASE_DIR, 'media'),
]

#configuracion ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': 900,
    },
}

PAYPAL_CLIENT_ID = 'AYDK3cPK2HdZQKJCsbyiRjk717_Wvc0sugQeC9FlXEVknSfblr1aknwzkc6pU5LyRgymuh71QgrObGym'
PAYPAL_CLIENT_SECRET = 'EMvCw8isi-BlBXiIAifOAmQZwp0YRKRcQhcAn1QU-kobstZ1a4opomulmtiRUce2ALeOTWd_7TZuz1bH'
PAYPAL_MODE = 'sandbox'  # Puede ser 'live' en producción

SECURE_CROSS_ORIGIN_OPENER_POLICY = {
    'same-origin': "'self'",
    'unsafe-none': None,
    'same-origin-allow-popups': "'self' allow-popups",
}


# settings.py
LOGIN_URL = 'login'
