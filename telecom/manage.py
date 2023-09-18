#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# -----------------------------------------------------------------------------------------------------------------------------------------------
import os  # Import the os module
import sys  # Import the sys module
from django.core.management import execute_from_command_line  # Import the execute_from_command_line function
# -----------------------------------------------------------------------------------------------------------------------------------------------
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings') # Set the Django settings module
    execute_from_command_line(sys.argv) # Execute the command line
# -----------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__': # If the name of the module is '__main__'
    try:
        main()
    except ImportError as exc: # If there is an import error
        raise ImportError( # Raise an import error
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you"
            "forget to activate a virtual environment?"
        ) from exc # From the exception
# -----------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------