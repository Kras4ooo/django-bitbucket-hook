import os
os.environ['DJANGO_SETTINGS_MODULE'] = "django_bitbucket_hook.settings"

from django.test.utils import setup_test_environment
setup_test_environment()

# Django 1.7
import django
if hasattr(django, 'setup'):
    django.setup()

from django.core.management import call_command
call_command('migrate')
