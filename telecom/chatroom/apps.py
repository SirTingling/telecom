# Importing the necessary django apps class for app configuration from Django
from django.apps import AppConfig

# Custom configuration class for the 'app' module
class AppConfiguration(AppConfig):
    """Configuration for the 'chatroom' module."""
    
    # name of the chatroom app
    name = 'chatroom' # This is the name of the chatroom app as it will be used in the Django project
    default_auto_field = 'django.db.models.BigAutoField' # This is the default auto field for the chatroom app