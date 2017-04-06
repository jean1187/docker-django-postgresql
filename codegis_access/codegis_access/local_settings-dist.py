# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9#hg_lpzo(a_50f4$rcslqh_9!_(u4rif^e$wj#a71^ncu22o5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Emails settings
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS       = True
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587

# Email data for send emails under this account
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_TO_EMAIL    = ''

# Admin server, by default Django put root@localhost
SERVER_EMAIL        = ''

# List of admins that can see the traceback errors when DEBUG = False
ADMINS              = [] # structure: [('Name', 'somebody@domain')]


DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',
        'NAME'    : 'db_name',
        'USER'    : 'db_user',
        'PASSWORD': 'db_password',
        'HOST'    : 'localhost',
        'PORT'    : '5432'
    }
}

# APPs USED ONLY IN DEVELOP
DEV_INSTALLED_APPS = ()
