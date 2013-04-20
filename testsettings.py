DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'taggit',
    'south',
    'nscms.simplenews',
    'nscms.simplenewsletter',
    'django.contrib.contenttypes',
)

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = ''
