from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a&3+0t=32fxqhxb=p)w)1a5+$te$qc6zt52yt28@5ss9h-t*_!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'account',
    'filed', 
    
    # 'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "crispy_forms",
    "crispy_bootstrap5",


    # API SetUp
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    "corsheaders",

    # 'drf_yasg',
    # 'django_filters',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASE_URL = "postgresql://postgres:YoHI7XoGpyVidDV0aRTE@containers-us-west-68.railway.app:7970/railway"
# DATABASES = {
#     'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
# }

# DATABASES = {  
#     'default': {  
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': 'crmdb',  
#         'USER': 'root',  
#         'PASSWORD': '',  
#         'HOST': '127.0.0.1',  
#         'PORT': '3306',
#     }  
# }  


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ACCOUNT_NUMBER_START_FROM = 1000000000

AUTH_USER_MODEL = 'account.User'
# AUTHENTICATION_BACKENDS = ['account.backends.EmailBackend'] # new

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
LOGOUT_URL = 'logout'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# email sending
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "mail.sanvicenteantioquia.com"
# # EMAIL_PORT = 993
# EMAIL_HOST_USER = 'radicacion@sanvicenteantioquia.com'
# EMAIL_HOST_PASSWORD = 'Email.2023' 
# # EMAIL_HOST_USER = 'dakaraefe2@gmail.com'
# # EMAIL_HOST_PASSWORD = 'lekfpooeqpwrkfps' 
# # EMAIL_HOST_PASSWORD = 'lekfpooeqpwrkfps' 
# # EMAIL_HOST_PASSWORD = '@emeritusroy2' 
# EMAIL_PORT = 995
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = True
EMAIL_HOST = "mail.sanvicenteantioquia.com"
EMAIL_HOST_USER = "radicacion@sanvicenteantioquia.com"
EMAIL_HOST_PASSWORD = "Email.2023"
EMAIL_PORT = 465
# EMAIL_USE_TLS = False


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"



############ All Api Rest Connection's ########
############ All Api Rest Connection's ########

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}



CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]