# ASGI configuration for the telecom project.
# This config exposes the ASGI callable as a module-level variable named `application`.

# Essential imports for ASGI configuration ------------------------------------------------------------------------------------------ >>
import os # Import the os module
from channels.routing import ProtocolTypeRouter, URLRouter # Import the ProtocolTypeRouter and URLRouter classes from channels.routing
from channels.auth import AuthMiddlewareStack # Import the authentication middleware stack
from django.core.asgi import get_asgi_application # Import the Django ASGI application
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Importing the sockets module from the chat app for handling websocket routes
import chatroom.routing
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Setting the default Django settings module to ensure the proper configuration is loaded when the ASGI server starts.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Here, I define how different types of connections will be handled.
# HTTP requests are directed to Django's ASGI application and websocket requests are passed through the authentication middleware stack 
# before being directed to the appropriate route in the chat application feature:
application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Route HTTP requests to Django's ASGI app
    'websocket': AuthMiddlewareStack(
        URLRouter(chatroom.routing.websocket_routes)  # Route websocket connections to chat app's routes
    )
}) # -----------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------- >>
