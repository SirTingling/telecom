# import serializers module from rest_framework
from rest_framework import serializers # Import the serializers module from Django Rest Framework
from .models import Interface, InterfaceContent  # Specify individual model imports
from memberProfiles.serializers import UserProfileSerializer  # memberProfile app's UserProfileSerializer

# Serializer to convert chatroom model instances into JSON format for API responses.
class ChatroomModelSerializer(serializers.ModelSerializer):
    # Represents the members of the chatroom using the UserProfileSerializer, 
    # allowing for detailed user information to be serialized along with chatroom details.
    user = UserProfileSerializer(many=True)

    class Meta:
        model =Interface
        fields = ['id', 'chatroom', 'user']

# Serializer for handling messages within a chatroom. 
# Transforms InterfaceContent model instances into JSON format for API responses.
class MessageModelSerializer(serializers.ModelSerializer):
    # Using UserProfileSerializer to represent the user who posted the message.
    posted_by = UserProfileSerializer()
    # Embedding detailed chatroom information using the ChatroomModelSerializer.
    associated_chatroom = ChatroomModelSerializer()

    class Meta:
        model = InterfaceContent
        fields = ['id', 'content', 'timestamp', 'user', 'chatroom']


