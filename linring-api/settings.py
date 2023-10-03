"""
Django settings for linring-api accounts.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from firebase_admin import credentials, initialize_app
from google.auth import load_credentials_from_file

# Build paths inside the accounts like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u26w5j74+fgytu$e6$bem-u8o)yfc#jw5-i4o5rwfjlm1a$*4f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'accounts.apps.AccountsConfig',
    'chat.apps.ChatConfig', # 채팅 앱
    'corsheaders',
    "fcm_django"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'linring-api.urls'  #project setting에 알맞게 수정 필요

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.get_url_front',
            ],
        },
    },
]

WSGI_APPLICATION = 'linring-api.wsgi.application'


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

LANGUAGE_CODE = 'ko-KR'
LANGUAGES = [
    ('ko-KR', "한국어"),
    ('ja', "일본어"),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

URL_FRONT = "http://localhost:3000" #customize your project url

AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
REGISTER_REDIRECT_URL = "/signup/complete"

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = URL_FRONT + REGISTER_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = URL_FRONT + REGISTER_REDIRECT_URL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'                   # 메일 호스트 서버
EMAIL_PORT = 587
EMAIL_HOST_USER='teamlinring@gmail.com'
EMAIL_HOST_PASSWORD='wxszuoftetoqvdyt'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = 'no-aply@email.com' # 커스텀 이메일 주소
DEFAULT_FROM_EMAIL = SERVER_EMAIL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[커스텀 메일 prefix] '

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'utils.pagination.StandardResultsSetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

REST_USE_JWT = True
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    "UPDATE_LAST_LOGIN": True,
    "TOKEN_REFRESH_SERIALIZER": "accounts.serializers.UpdateTokenRefreshSerializer",
}
TOKEN_REFRESH_SERIALIZER = "accounts.serializers.UpdateTokenRefreshSerializer"
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False,
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserDetailSerializer',
    'REGISTER_SERIALIZER': 'accounts.serializers.UserRegisterSerializer',
    'LOGOUT_ON_PASSWORD_CHANGE': False
}

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CSRF_TRUSTED_ORIGINS = ["https://api.", "https://", "http://192.168.0.208","http://localhost:3000"] # add custom your url


# To learn more, visit the docs here:
# https://cloud.google.com/docs/authentication/getting-started>
class CustomFirebaseCredentials(credentials.ApplicationDefault):
    def __init__(self, account_file_path: str):
        super().__init__()
        self._account_file_path = account_file_path

    def _load_credential(self):
        if not self._g_credential:
            self._g_credential, self._project_id = load_credentials_from_file(self._account_file_path,
                                                                              scopes=credentials._scopes)


# init default firebase app
# this loads the default google service account with GOOGLE_APPLICATION_CREDENTIALS env variable
FIREBASE_APP = initialize_app()

# init second firebase app for fcm-django
# the environment variable contains a path to the custom google service account JSON
custom_credentials = CustomFirebaseCredentials(
    os.path.join(BASE_DIR, 'linring-a3e66-firebase-adminsdk-vumb7-53e3e56fc8.json')) #custom url json path
FIREBASE_MESSAGING_APP = initialize_app(custom_credentials, name='messaging')
FCM_DJANGO_SETTINGS = {
    # an instance of firebase_admin.App to be used as default for all fcm-django requests
    # default: None (the default Firebase app)
    "DEFAULT_FIREBASE_APP": FIREBASE_MESSAGING_APP,
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "FCM 장치 관리",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": True,
}
# S3_BUCKET = "s3 bucket name"

# AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET
# AWS_S3_BUCKET_NAME = S3_BUCKET
# AWS_REGION = 'ap-northeast-2'
# STATIC_URL = "https://static.gamept.gg/"
# MEDIA_URL = "https://static.gamept.gg/media"

# STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
# DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'

AWS_DEFAULT_ACL = None
CHAT_UNIQUE_ROOM = False

# ACCOUNT_LOGOUT_ON_GET = True