"""
Django settings for jcotechy project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
# import os
# from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv() #Note that by default python-dontenv package passes the .env as a path to load_dotenv function to retreive all .env files using either os.getenv(file variable name) or os.environ.get(file variable name)
# also note that, os.environ.get(variable name) fetches it as a dictionary while os.getevn(variable name) fetches it as a assigned value.

# load_dotenv(BASE_DIR / 'env'), alternative 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']
print("print debug value ##############################")
print(os.getenv('DEBUG'))


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

# superuser authentication configuration
ADMIN_USER = os.environ.get('ADMIN_USER')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWD')

# Application definition

INSTALLED_APPS = [
    # integrated library apps
    'jazzmin', #custom admin interface
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'blog',
    'core',
    'account',
    # integrated library apps
    # 'admin_interface',
    # 'colorfield',
    'tinymce',
    'ckeditor',
    'django_social_share',
    'storages',
    

]

MIDDLEWARE = [
    #default security middleware
     'django.middleware.security.SecurityMiddleware',
     #whitenoise middleware for static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware',
     #other default middlewares
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jcotechy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
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

WSGI_APPLICATION = 'jcotechy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    #configure render postgres database for deployment
    import dj_database_url
    
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#Email configurations
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'youremail@gmail.com'  
EMAIL_HOST_PASSWORD = 'yourpassword'  
EMAIL_PORT = 587 


#browser login session expiration settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # opional, as this will log you out when browser is closed
SESSION_COOKIE_AGE = 1800                  # 0r 5 * 60, same thing
SESSION_SAVE_EVERY_REQUEST = True          # Will prevent from logging you out after 300 seconds

#configure cookie settings for production
# SECURE_SSL_REDIRECT=True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SAMESITE = 'None'
#SESSION_COOKIE_SAMESITE = 'None'



# AWS CONFIFURATION SETTINGS FOR MEDIA FILES
if not DEBUG:
    try:
        """
        using AWS setup for django media files
        """
        print("##############################")
        print("---------using AWS storage system----------------")
        print("##############################")

        """
        SHOW AWS STATIC LOGGINGS ON UPLOADING FILES
        """
        import logging

        logger = logging.getLogger('boto3')
        logger.setLevel(logging.INFO)
       
       
        # aws settings
        AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
        AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

        # AWS_DEFAULT_ACL = "public-read"
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
        AWS_HEADERS= {
            'Access-Control-Allow-Origin':'*',
        }
        # TEXT_CKEDITOR_BASE_PATH = 'https://%s/djangocms_text_ckeditor/ckeditor/' % AWS_S3_CUSTOM_DOMAIN


        # S3 Static and Media Files Storage
        DEFAULT_FILE_STORAGE = 'custom_storage.MediaStorage'
        # 'storages.backends.s3boto3.S3Boto3Storage'
        # AWS_S3_FILE_OVERWRITE = True
        # AWS_DEFAULT_ACL = 'public-read'

        # S3 Media Files Storage
        AWS_MEDIA_LOCATION = 'media'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'


        # S3 Static Files Storage
        # STATICFILES_DIRS = [BASE_DIR/'static']
        # STATIC_LOCATION = 'static'
        # STATICFILES_STORAGE = 'custom_storage.StaticStorage'
        # 'storages.backends.s3boto3.S3Boto3Storage'
        # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
        # AWS_STATIC_LOCATION = 'static'
        # 'custom_storage.StaticStorage'
        """
        use whitenoise alternatively for static files storage and compression in production
        """ 
        # Using whitenoise  static settings
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [BASE_DIR/'static']
        STATIC_ROOT = BASE_DIR/'staticfiles'
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
   

       
        

        #ckeditor 
                # CKEDITOR_CONFIGS = {
                # "default": {
                #     "removePlugins": "stylesheetparser",
                # }
                # }
                # AWS_QUERYSTRING_AUTH = False
        # CKEDITOR_BROWSE_SHOW_DIRS = True
        # CKEDITOR_RESTRICT_BY_USER = True
        # CKEDITOR_RESTRICT_BY_DATE = False
        #CKEDITOR_BASEPATH = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STORAGE_BUCKET_NAME}/{STATIC_LOCATION}/ckeditor/ckeditor/"
        #"https://blogteck.s3.us-east-2.amazonaws.com/static/ckeditor/ckeditor/"
        # TEXT_CKEDITOR_BASE_PATH = 'https://%s/djangocms_text_ckeditor/ckeditor 
    except:
        pass
else:
# except:
    """
    use local setup for django static and media files
    """
    print("-------------using LOCAL SETUP-------------")

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    # local static settings
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR/'static']
    STATIC_ROOT = BASE_DIR/'staticfiles'
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    # local mediafiles settings (user uploaded files)
    MEDIA_URL = '/media/'
    # Absolute filesystem path to the directory that will hold user-uploaded files locally.
    MEDIA_ROOT = BASE_DIR/ 'media/'
    
    # DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# Account login and redirect url

LOGIN_URL='account/signin'
LOGIN_REDIRECT_URL='account/profile'





# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEDITOR CONFIFURATION SETTINGS

# URL to the directory where the CKEditor JavaScript files are stored
CKEDITOR_BASEPATH = STATIC_URL + "ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
     'default': {
    #     'toolbar': 'Custom',
    #     'toolbar_Custom': [
    #         ['Bold', 'Italic', 'Underline'],
    #         ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
    #         ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
    #         ['Link', 'Unlink'],
    #         ['RemoveFormat', 'Source'],
    #         ['Maximize', 'ShowBlocks'],
    #     ],
        'width': '100%',
        'height': 300,
        # 'filebrowserWindowWidth': 940,
        # 'filebrowserWindowHeight': 725,
        # 'extraPlugins': 'image2,video',
    }
}



# TINYMCE CONFIFURATION SETTINGS
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': "100%",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
        textcolor save link image media preview codesample contextmenu
        table code lists fullscreen  insertdatetime  nonbreaking
        contextmenu directionality searchreplace wordcount visualblocks
        visualchars code fullscreen autolink lists  charmap print  hr
        anchor pagebreak
    ''',
    'toolbar1': '''
        fullscreen preview bold italic underline | fontselect,
        fontsizeselect  | forecolor backcolor | alignleft alignright |
        aligncenter alignjustify | indent outdent | bullist numlist table |
        | link image media | codesample |
    ''',
    'toolbar2': '''
        visualblocks visualchars |
        charmap hr pagebreak nonbreaking anchor |  code |
        ''',
    'contextmenu': 'formats | link image',
    'menu': '[]',
    'statusbar': 'false',
}
