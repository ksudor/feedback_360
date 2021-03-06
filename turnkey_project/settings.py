"""
Django settings for projectname project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2s654i9DKQO>fl^XifO(mX_H{5tzG@F:a}Qo!wP=7w^g5[h6H9[zyWowc_pm>>gV'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (TEMPLATE_PATH,)


with open('/var/lib/django/allowed_hosts', 'r') as fob:
    # Read allowed_hosts dynamically for reliable inithooks host setting
    ALLOWED_HOSTS = [line.rstrip() for line in fob]

#For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False



#Webmail �����https://webmail.adm.tools/
#��� ������������fedback360@998899.xyz
#������:	69bOI7yfa0YV
#POP3/IMAP ������:	mail.adm.tools
#POP3 ����:	110 ��� 995 (POP3+SSL)
#IMAP ����:	143 ��� 993 (IMAP4+SSL)
#SMTP ������:	mail.adm.tools
#SMTP ����:	25 ��� 2525 ��� 465 (SMTP+SSL)

EMAIL_HOST = 'mail.adm.tools'

EMAIL_HOST_USER = 'feedback360@998899.xyz'

#Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = '69bOI7yfa0YV'

EMAIL_PORT = 25

#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#EMAIL_HOST = "localhost"
#EMAIL_PORT = "25"
#DEFAULT_FROM_EMAIL = "noreply@example.com"



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'askfeedback',
    'leavefeedback',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'turnkey_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
         ],
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

WSGI_APPLICATION = 'turnkey_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'fbebd32a51ab8277be0ef80004d4982c',
    }
}

 


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
