"""
WSGI config for telecom advanced web dev project.
It exposes the WSGI callable as a module-level variable named ``appication``.
"""
# -----------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------
import os # Import the OS module
from django.core.wsgi import get_wsgi_application # Import the Django WSGI application

def get_telecom():
    # Set the Django settings module for the WSGI application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # Return the WSGI telecom app
    return get_wsgi_application()

# Get the WSGI app
application = get_telecom()
# -----------------------------------------------------------------------------------------------------------------------------------------------