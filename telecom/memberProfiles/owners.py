from django.contrib import admin # Import the admin module from Django admin for admin configurations
from .models import UserProfile  # Import the UserProfile model from the models.py file in the same directory as this file

# Admin configurations

class MemberProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserAccount model.
    """
    info_display = ('user', 'image', 'phone_number', 'dob') # The fields to be displayed in the admin portal

# Register the model with its respective admin configuration
admin.site.register(UserProfile, MemberProfileAdmin)

