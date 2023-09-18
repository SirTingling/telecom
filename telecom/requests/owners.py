from django.contrib import admin
from .models import Friend, FriendshipRequest


# Admin configuration for managing friends in the admin interface
class FriendManagementAdmin(admin.ModelAdmin):
    # Fields to filter results in the admin interface
    info_filter = ['id', 'current_user']

    # Fields to display in the main list view in the admin interface
    info_display = ['id', 'current_user']

    # Fields to search in the admin interface
    search_fields = ['id', 'current_user']

    # Linking this configuration to the Friend model
    class Meta:
        model = Friend

# Admin configuration for managing friend requests in the admin interface
class FriendRequestManagementAdmin(admin.ModelAdmin):
    # Fields to filter results in the admin interface
    info_filter = ['id', 'sender', 'receiver', 'pending']

    # Fields to display in the main list view in the admin interface
    info_display = ['id', 'sender', 'receiver', 'pending']

    # Fields to search in the admin interface
    search_fields = [
        'sender__username', 'sender__email',
        'receiver__username', 'receiver__email'
    ]

    # Linking this configuration to the FriendshipRequestmodel
    class Meta:
        model = FriendshipRequest

# Linking models to their respective admin configurations
admin.site.register(Friend, FriendManagementAdmin)
admin.site.register(FriendshipRequest, FriendRequestManagementAdmin)
