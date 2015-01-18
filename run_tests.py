#!/usr/bin/env python

import sys

from django.conf import settings


def main():
    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'nscms',
            'nscms.contrib.newsletter',
        ],
        DATABASE_ENGINE='django.db.backends.sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        MEDIA_ROOT='/tmp/nscms_test_media/',
        MEDIA_URL='/media/',
        STATIC_URL="/static/",
        ROOT_URLCONF='nscms.tests.urls',
        DEBUG=True,
        TEMPLATE_DEBUG=True,
    )

    from django.test.utils import get_runner
    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failures = test_runner.run_tests(['nscms', 'nscms.contrib.newsletter'])
    sys.exit(failures)


if __name__ == '__main__':
    main()
