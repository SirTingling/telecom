# rest framework import of serializers to be used in the views
from rest_framework import serializers # Importing the serializers module from the Django REST framework
from .models import * # Importing all models from the memberProfiles app

# Serializer for the User model
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the details of the User model.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,  # Ensures that password is not visible when reading data
                'style': {'input_type': 'password'}  # This Renders it as a password field when collecting input
            }
        }

# Serializer for the UserProfile model
class UserProfileDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the details of the UserProfile model along with related User details.
    """
    
    # Use the above UserProfileDetailSerializer to serialize the associated user
    user = UserProfileSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'image', 'phone_number', 'dob']
