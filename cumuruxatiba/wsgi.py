"""
WSGI config for cumuruxatiba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cumuruxatiba.settings")

application = get_wsgi_application()
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cumuruxatiba.settings")


application = get_wsgi_application()



>>>>>>> 372fb89680b88e5dd6fb36c75288ade693f18f8f
