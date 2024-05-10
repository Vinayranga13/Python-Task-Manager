import os
from django.core.wsgi import get_wsgi_application

# Default Django settings module 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskManager.settings")

# Get the WSGI application object.
application = get_wsgi_application()
