# importing the serializers module from the Django REST framework
from rest_framework import serializers # Importing the serializers module from the Django REST framework
from .models import * # Importing all models from the requests app
from memberProfiles.serializers import * # Importing the serializers module from the memberProfiles app
# Serializer for the User model
# --------------------------------------------------------------------------------------------------------------- >> 
# Serializer for the Friend model
class UserWithFriendsSerializer(serializers.ModelSerializer):
    """
    UserWithFriendsSerializer:
    A serializer to represent the association of a user with their list of friends. 
    """
    current_user = UserProfileSerializer()
    friends = UserProfileSerializer(many=True)
    class Meta:
        model = Friend
        fields = ['pk', 'current_user','friends']
# --------------------------------------------------------------------------------------------------------------- >>
# Serializer for the FriendshipRequest model
class FriendshipInteractionSerializer(serializers.ModelSerializer):
    """
    FriendshipInteractionSerializer:
    A serializer to provide detailed representation of a friend request, 
    highlighting the sender, receiver, and the state of the request.
    """
    sender = UserProfileSerializer()
    receiver = UserProfileSerializer()
    class Meta:
        model = FriendshipRequest
        fields = ['pk', 'sender', 'receiver', 'pending', 'timestamp']
# --------------------------------------------------------------------------------------------------------------- >>
