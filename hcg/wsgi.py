"""
WSGI config for hcg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

print("WSGI script started")  # Debug statement

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hcg.settings')
print("DJANGO_SETTINGS_MODULE:",
      os.environ['DJANGO_SETTINGS_MODULE'])  # Debug statement

application = get_wsgi_application()
print("WSGI application loaded")  # Debug statement
