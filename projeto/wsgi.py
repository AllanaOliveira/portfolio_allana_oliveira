"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = get_wsgi_application()

import os

import sys

## assumindo que sua aplicação django está em '/home/UFFCarlosRibeiro/projeto/projeto/prod.py'

## e que seu manage.py está em '/home/UFFCarlosRibeiro/projeto/manage.py'

path = 'D:\Allan\Documents\Projetos Django\portfolio\portfolio\projeto'
if path not in sys.path:

    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'produto.prod'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
