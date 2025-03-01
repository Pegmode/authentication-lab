#!/usr/bin/env python
import os
import sys
from django.conf import settings


if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authlab.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    settings.ALLOWED_HOSTS=['*',]#this is bad normally but I could care less for a lab. I'd rather work on a remote machine thank you very much
    execute_from_command_line(sys.argv)

