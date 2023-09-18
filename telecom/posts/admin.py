# Importing necessary modules from Django's framework
from django.contrib import admin # Importing the admin module from Django admin for admin configurations
from .models import UserArticle # Importing the UserArticle model from the models.py file in the same directory as this file

# Defining a custom admin class to customize how UserArticle objects are displayed in the admin panel
class PostAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    info_display = ('id', 'user', 'content', 'content_image', 'timestamp')

# Registering the UserArticle model with the admin site using the custom admin class
admin.site.register(UserArticle, PostAdmin)
