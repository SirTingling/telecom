# Importing the necessary django apps class for app configuration from Django
from django.apps import AppConfig

# Custom configuration class for the 'app' module
class AppConfiguration(AppConfig):
    """Configuration for the 'posts' module."""
    
    # name of the posts app
    name = 'posts' # This is the name of the posts app as it will be used in the Django project
    default_auto_field = 'django.db.models.BigAutoField' # This is the default auto field for the posts app