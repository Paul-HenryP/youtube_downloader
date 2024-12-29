"""
WSGI config for youtube_downloader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

project_path = '/home/PaulHenryP/youtube_downloader'
if project_path not in sys.path:
    sys.path.append(project_path)

# Point to the settings module.
os.environ['DJANGO_SETTINGS_MODULE'] = 'youtube_downloader.settings'

# Import the WSGI application.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

