# import the required modules
import factory # import the factory module
from .models import *
from memberProfiles.factories import MockUserFactory

# MockChatroomFactory
# Factory to create mock instances of Chatroom for testing purposes.
class MockChatroomFactory(factory.django.DjangoModelFactory):
    # Sample name for the chatroom
    name = 'test_chatroom' 

    # Metadata class provides metadata to the factory
    class Meta:
        model = Interface  # Linking to the Chatroom model

# InterfaceContentFactory
## InterfaceContentFactory: Used for creating mock chat messages for testing purposes.
class InterfaceContentFactory(factory.django.DjangoModelFactory):
    
    # Sample content for the chat message
    content = "chat_msg_1"  # Used underscore for consistency
    
    # Sample timestamp for the message
    timestamp = factory.Faker('date_time')  # Using factory's Faker to generate realistic date times

    # Associate the chat message with a user
    user = factory.SubFactory(MockUserFactory)
    
    # Associate the chat message with a chatroom
    chatroom = factory.SubFactory(MockChatroomFactory)

    # Metadata class provides metadata to the factory
    class Meta:
        model = InterfaceContent  # Linking to the InterfaceContent model
