# loading the test environment
from django.test import TestCase # Django's base test case class
from django.urls import reverse # Django's reverse function for URL lookups
import json # Python's built-in JSON module
# Local module imports
from .models import * # Import all models from the models.py file in the same directory as this file
from .factories import * # Import all factories from the factories.py file in the same directory as this file
from .views import * # Import all views from the views.py file in the same directory as this file
from .serializers import * # Import all serializers from the serializers.py file in the same directory as this file
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# ChatroomModelTestCase
# This class focuses on testing the Chatroom model. It ensures that instances of the Chatroom model
# have the correct data, and that the associated API behaves as expected.
class ChatroomModelTestCase(TestCase):
    chatroom = None
    ChatroomModelSerializer = None

    def setUp(self):
        """
        Setup method is run before every test method to set up any objects 
        or states that might be needed during testing.
        """
        # Create a chatroom instance using the ChatroomFactory
        self.chatroom = MockChatroomFactory.create()
        self.ChatroomModelSerializer = ChatroomModelSerializer(instance=self.chatroom)
         # Define valid and invalid endpoints for testing the API.
        self.good_url = reverse('chatroom_detail_api', kwargs={'pk': 1})
        self.bad_url = "api/chatroom/qwerty"

    def tearDown(self):
        """
        Teardown method is run after every test method to cleanup 
        any objects or reset states to avoid any conflicts with subsequent tests.
        """
        # Delete all Chatroom instances and reset factory sequence.
        Interface.objects.all().delete() # Delete all Chatroom instances.
        MockChatroomFactory.reset_sequence() # Reset factory sequence.

    # test that the data in the model matches the details
    def test_chatroom_instance_data(self): 
        """Check if the Chatroom instance has the correct attributes and associated data."""
        chatroom = self.chatroom # Get the chatroom instance created in the setUp method.
        self.assertIsInstance(chatroom, Interface) # Check if the chatroom instance is of type Chatroom.
        """ it does, so the test passes and the test method ends here. """
        self.assertEqual(chatroom.chatroom, 'testchatroom')

    # test that the view returns correct code with redirect
    def test_chatroom_view_status_code(self):
        """Ensure that accessing the chatroom view returns the expected redirect status code."""
        response = self.client.get(reverse('chat')) # Get the response from the chatroom view.
        self.assertEqual(response.status_code, 302) # Check if the response status code is 302.
    # test that the view returns correct code with redirect
    def test_serializer_output(self): ##########################################
        """Check if the Chatroom outputs produces the correct fields."""
        expected_fields = set(['pk', 'chatroom', 'user'])
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    # test that api returns correct fields when success
    def test_chatroom_serializer(self): 
        """Check if the Chatroom serializer produces the correct fields."""
        data = self.ChatroomModelSerializer.data # Get the data from the Chatroom serializer.
        self.assertEqual(set(data.keys()), set(['pk', 'chatroom', 'user'])) # Check if the serializer has the correct fields.

    # the test that api returns correct fields when success
    def test_api_response_success(self):
        """Validate that a GET request to a valid API endpoint returns the correct response.""" 
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint.
        response.render() # Render the response as JSON.
        self.assertTrue(response.status_code, 200) # Check if the response status code is 200 and if it is, the test passes.
        data = json.loads(response.content) # Load the response content as JSON.

        # api has these fields
        self.assertTrue(data['pk'])
        self.assertTrue(data['chatroom'])

    # the testing of the api returns correct fields when error
    def test_api_response_failure(self):
        """Verify that a GET request to an invalid endpoint returns a 404 error."""
        response = self.client.get(self.bad_url, format='json') # Get the response from the API endpoint.
        self.assertTrue(response.status_code, 404) # Check if the response status code is 404 and if it is, the test passes.

    def test_chatroom_count(self):
        """Ensure that when a new Chatroom instance is created, the count of chatrooms increases by one."""
        initial_count = Interface.objects.count() # Get the initial count of Chatroom instances.
        MockChatroomFactory.create() # Create a new Chatroom instance.
        new_count = Interface.objects.count() # Get the new count of Chatroom instances.
        self.assertEqual(initial_count + 1, new_count) # Check if the new count is equal to the initial count + 1.

# InterfaceContentModelTestCase
# This class focuses on testing the InterfaceContent model. It ensures that instances of the 
# InterfaceContent model have the correct data, and that they are created and ordered as expected.
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
class InterfaceContentModelTestCase(TestCase):
    """
    Setup for InterfaceContent tests.
    """
    # Create a InterfaceContent instance for testing purposes.
    chatroomContent = None
    ChatroomModelSerializer = None

    def setUp(self):
        """
        Setup for InterfaceContent tests.
        """

        # Create a InterfaceContent instance for testing purposes.
        # Define valid and invalid endpoints for testing the API.
        self.chatroomContent = InterfaceContentFactory.create() # Create a InterfaceContent instance using the InterfaceContentFactory.
        self.MessageModelSerializer = MessageModelSerializer() # Create a MessageModelSerializer instance.
        # Define valid and invalid endpoints for testing the API.
        self.good_url = reverse('chatroom_detail_api', kwargs={'pk': 1}) # Define a valid endpoint for testing the API.
        self.bad_url = "api/chatroom/qwerty" # Define an invalid endpoint for testing the API.

    def tearDown(self):
        """
        Cleanup after InterfaceContent tests.
        """
        # Delete all InterfaceContent instances and reset factory sequence.
        Interface.objects.all().delete() # Delete all InterfaceContent instances.
        InterfaceContent.objects.all().delete() # Delete all InterfaceContent instances.
        MockChatroomFactory.reset_sequence() # Reset factory sequence.
        InterfaceContentFactory.reset_sequence() # Reset factory sequence.
        # -------------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test that the data in the model matches the details
    def test_chatroom_content_instance_data(self):
        """
        Ensure that the InterfaceContent instance has the expected attributes and associated data.
        This test dives into nested attributes (e.g., user's username) to ensure data integrity.
        """
        chatroomContent = self.chatroomContent # Get the InterfaceContent instance created in the setUp method.
        self.assertIsInstance(chatroomContent, InterfaceContent) # Check if the InterfaceContent instance is of type InterfaceContent.
        # Check if the InterfaceContent instance has the expected attributes and associated data.
        self.assertEqual(chatroomContent.content, 'chat msg 1')
        self.assertEqual(chatroomContent.user.username, 'jamesbond007')
        self.assertEqual(chatroomContent.user.email, 'jamesbond@outlook.com')
        self.assertEqual(chatroomContent.user.first_name, 'james')
        self.assertEqual(chatroomContent.user.last_name, 'bond')
        self.assertEqual(chatroomContent.user.password, 'w007')
        self.assertEqual(chatroomContent.chatroom.chatroom, 'testchatroom')
        # -------------------------------------------------------------------------------------------------------------------------------------------------- >>
        """
        Ensure that the InterfaceContent instance has the expected attributes and associated data.
        """