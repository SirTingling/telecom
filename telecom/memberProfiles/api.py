# Django imports
from .forms import RegistrationUserForm # Import the RegistrationUserForm from the form.py file
from .models import * # Import all models from the models.py file
from .serializers import UserProfileSerializer, UserProfileDetailSerializer # Import the UserProfileSerializer and UserProfileDetailSerializer from the serializers.py file
# -----------------------------------------------------------------------------------------------------------------------------------------------
# DRF (Django Rest Framework) imports
from rest_framework import generics, mixins

class UserProfileListView(generics.ListAPIView):
    """
    UserProfileListView serves as an API endpoint for listing all user profiles.

    This view inherits from ListAPIView, which is a concrete generic API view
    provided by Django Rest Framework for displaying a list of objects.

    Attributes:
        queryset: Specifies the dataset of UserProfile objects to work with.
        serializer_class: Defines the serializer to represent the UserProfile data.
    """
    queryset = UserProfile.objects.all()  
    serializer_class = UserProfileDetailSerializer 


class UserCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    """
    UserCreateView serves as an API endpoint to create new users.

    This view combines the functionalities of GenericAPIView for core functionality
    and CreateModelMixin to add object creation via POST method.

    Attributes:
        queryset: Specifies the dataset of User objects to work with.
        serializer_class: Defines the serializer to represent the User data.
        form_class: Uses the UserForm for additional validation or fields during creation.

    Methods:
        post: Handles the POST request to create a new User instance.
    """
    queryset = User.objects.all()  
    serializer_class = UserProfileSerializer
    form_class = RegistrationUserForm  

    def post(self, request, *args, **kwargs):
        """Handles the POST request to instantiate and save a new User."""
        return self.create(request, *args, **kwargs)


class UserProfileDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    """
    UserProfileDetailView serves as an API endpoint to fetch details of a specific user profile.

    This view combines the functionalities of GenericAPIView for core functionality
    and RetrieveModelMixin to fetch details of an object.

    Attributes:
        queryset: Specifies the dataset of UserProfile objects to work with.
        serializer_class: Defines the serializer to represent the UserProfile data.

    Methods:
        get: Handles the GET request to retrieve details of the specified UserProfile instance.
    """
    queryset = UserProfile.objects.all()  
    serializer_class = UserProfileDetailSerializer  
    
    def get(self, request, *args, **kwargs):
        """Fetches and returns the details of a specified UserProfile instance."""
        return self.retrieve(request, *args, **kwargs)
