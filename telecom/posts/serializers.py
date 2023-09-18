# importing from the Django REST framework:
from rest_framework import serializers # Importing the serializers module from the Django REST framework
from .models import UserArticle  # Explicitly import the required model
from memberProfiles.serializers import UserProfileSerializer  # Explicitly import the required serializer from the memberProfiles app
# ------------------------------------------------------------------------------------------------------------------------------------------------------- >>
# Serializer for the UserArticle model. This is responsible for converting the UserArticle
# instances to JSON representation and vice-versa. This will be mainly used for API views.
class UserPostDetailSerializer(serializers.ModelSerializer):
    
    # Nested serialization: 
    # Instead of just returning the user's ID, I'm using the UserProfileSerializer
    # to provide more detailed information about the user in the serialized output.
    user = UserProfileSerializer(read_only=True)  # Marked as read_only to ensure nested updates aren't allowed

    class Meta:
        # Specify the model to which this serializer is associated
        model = UserArticle
        
        # Define the fields to be included in the serialized representation.
        fields = ['pk', 'user', 'content', 'content_image', 'timestamp']
# ------------------------------------------------------------------------------------------------------------------------------------------------------- >>
