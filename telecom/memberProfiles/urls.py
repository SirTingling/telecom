# Path: telecom/memberProfiles/urls.py
# importing the path function from Django
from django.urls import path # Importing the path function from Django
from django.conf import settings # Importing the settings module from Django
from django.conf.urls.static import static # Importing the static module from Django
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
from . import views # Importing the views module from the memberProfiles app
from . import api # Importing the API views module from the memberProfiles app
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# Defining URL patterns for the memberProfiles app

# User management views' URL patterns
user_management_patterns = [
    # Registration page URL pattern
    path('register/', views.register_new_user, name='register_new_user'),

    # Login page URL pattern
    path('login/', views.login_user, name='login_user'),

    # User profile page URL pattern
    path('profile/', views.display_user_profile, name='display_user_profile'),

    # Edit profile page URL pattern
    path('edit-profile/', views.update_user_profile, name='update_user_profile'),

    # User search page URL pattern
    path('search/', views.search_for_users, name='search_for_users'),

    # Logout action URL pattern
    path('logout/', views.user_logout, name='user_logout'),

    # Accept friend request URL pattern
    path('accept-request/<req_id>/', views.approve_friend_request, name="approve_friend_request"),

    # Decline friend request URL pattern
    path('decline-request/<req_id>/', views.reject_friend_request, name="reject_friend_request"),
]

# User API-related URL patterns
api_urlpatterns = [
    # API endpoint to list all users
    path('api/user/', api.UserProfileListView.as_view(), name='UserProfileListView'),

    # API endpoint to view details of a specific user
    path('api/user/<int:pk>/', api.UserProfileDetailView.as_view(), name='UserProfileDetailView'), 

    # API endpoint to create a new user
    path('api/create-user/', api.UserCreateView.as_view(), name='UserCreateView'),
]

# Combining all URL patterns for clarity and organization
urlpatterns = user_management_patterns + api_urlpatterns

# Configuring static and media files' URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

