from django.contrib import admin
from .models import Interface, InterfaceContent

# Admin configuration for the Interface model
class InterfaceAdminConfig(admin.ModelAdmin):
    info_display = ['pk', 'chatroom']  # chatroom for the Interface model

# Admin configuration for the InterfaceContent model
class InterfaceContentAdminConfig(admin.ModelAdmin):
    info_display = ['content', 'timestamp', 'user', 'chatroom']  # content, timestamp, user, and chatroom for the InterfaceContent model

# Register models with their corresponding admin configurations
admin.site.register(Interface, InterfaceAdminConfig)
admin.site.register(InterfaceContent, InterfaceContentAdminConfig)
