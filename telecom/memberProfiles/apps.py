# Importing the necessary django apps class for app configuration from Django
from django.apps import AppConfig

# Custom configuration class for the 'memberProfile' module
class AppConfiguration(AppConfig):
    """Configuration for the 'memberProfile' module."""
    
    # name of the memberProfile app
    name = 'memberProfiles' # This is the name of the memberProfile app as it will be used in the Django project
    default_auto_field = 'django.db.models.BigAutoField' # This is the default auto field for the memberProfile app