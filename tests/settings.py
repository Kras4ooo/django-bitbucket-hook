SECRET_KEY = 'secret'
INSTALLED_APPS = (
    'django_bitbucket_hook',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = 'django_bitbucket_hook.urls'
