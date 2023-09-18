# importing the path function from Django and the views module from the posts app
from django.urls import path # Importing the path function from Django
from . import views # Importing the views module from the posts app
from . import api  # Importing the API module from the posts app
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# URL patterns for the app
# Here we define the routes for both the standard web views and the API endpoints

urlpatterns = [
    # Web views
    path('', views.home, name='home'),  # Endpoint for the main posts dashboard or listing
    
    # API views
    # Endpoints related to User Posts
    path('api/userposts/<int:pk>/', api.UserPostRetrieveView.as_view(), name='api_user_post_retrieve'), # Endpoint to retrieve a single UserPost instance based on its primary key
    path('api/createpost/', api.UserPostCreateView.as_view(), name='api_user_post_create'), #  ### names matching with the tests and the apis and the views
    # Endpoint to create a new UserPost instance
]
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
