#!/usr/bin/env python

"""
Adapted from django-constance, which itself was adapted from django-adminfiles.
"""

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(here)
sys.path[0:0] = [here, parent]

from django.conf import settings
settings.configure(
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}},
    SECRET_KEY = "it's a secret to everyone",
    INSTALLED_APPS = ["django_comments", "testapp", "custom_comments"],
)

from django.test.simple import DjangoTestSuiteRunner

def main():
    runner = DjangoTestSuiteRunner()
    failures = runner.run_tests(['testapp'], verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    main()