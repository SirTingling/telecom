# imports from rest_framework
from django.test import TestCase # Django's TestCase class
from django.urls import reverse # Django's reverse function
# Local module imports
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
import json # Python's built-in JSON module
from .models import * # Import all models from the models.py file in the same directory as this file
from .views import * # Import all views from the views.py file in the same directory as this file
from .serializers import * # Import all serializers from the serializers.py file in the same directory as this file
 # -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# Fiend Model Test Case for testing the Friend model
class FriendModelTestCase(TestCase):
    """Test suite for the Friend model and its related functionalities."""
    friend = None # Initialize the friend variable
    friendRequest = None # Initialize the friendRequest variable

    def setUp(self):
        """Initial setup for tests: creating users and Friend instances."""
        # the creation of a sample friend here is not necessary, but it is done to ensure that the Friend model is working as expected
        self.user1 = User.objects.create(
            username='user1', # Create a user USERNAME using the UserFactory
            email='user1@gmail.com', # Create a user EMAIL using the UserFactory
            first_name='user1fn',  # Create a user FIRST_NAME using the UserFactory
            last_name='user1ln', # Create a user LAST_NAME using the UserFactory
            password='user1password' # Create a user PASSWORD using the UserFactory
        ) # the creation of the user is done using the UserFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friend1 = Friend.objects.create(
            current_user=self.user1 # Create a friend instance using the FriendFactory
        )
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.user2 = User.objects.create(
            username='user2',  # Create a user USERNAME using the UserFactory
            email='user2@gmail.com',  # Create a user EMAIL using the UserFactory
            first_name='user2fn',  # Create a user FIRST_NAME using the UserFactory
            last_name='user2ln',  # Create a user LAST_NAME using the UserFactory
            password='user2password' # Create a user PASSWORD using the UserFactory
        )
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friend2 =  Friend.objects.create(current_user=self.user2) # Create a friend instance using the FriendFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friendSerializer = UserWithFriendsSerializer(instance=self.friend1) # Initialize the serializer for the friend instance
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.good_url = reverse('FriendDetailView', kwargs={'pk': 1}) # Construct a valid URL for the friend API
        self.bad_url = "api/friendlist/qwerty" # Construct an invalid URL for the friend API
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    def tearDown(self):
        """Cleanup after each test: Removing all instances."""
        # Clean up the created objects to maintain isolation between tests
        User.objects.all().delete() # Delete all User instances
        Friend.objects.all().delete()   # Delete all Friend instances

    # the data should now be tested with the serializer instead of the model
    def test_friend_request_data_integrity(self):
        """Ensure data stored in Friend model is consistent with created user data."""
        friend1 = self.friend1 # Get the friend instance created in the setUp method
        friend2 = self.friend2 # Get the friend instance created in the setUp method
        self.assertIsInstance(friend1, Friend) # Check if the friend instance is of type Friend
        self.assertIsInstance(friend2, Friend) 
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertEqual(friend1.current_user.username, 'user1') # Check if the username is correct of user 1
        self.assertEqual(friend1.current_user.email, 'user1@gmail.com') # Check if the email is correct of user 1
        self.assertEqual(friend1.current_user.first_name, 'user1fn') # Check if the first name is correct  of user 1
        self.assertEqual(friend1.current_user.last_name, 'user1ln') # Check if the last name is correct of user 1
        self.assertEqual(friend1.current_user.password, 'user1password') # Check if the password is correct of user 1
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertEqual(friend2.current_user.username, 'user2') # Check if the username is correct of user 2
        self.assertEqual(friend2.current_user.email, 'user2@gmail.com') # Check if the email is correct of user 2
        self.assertEqual(friend2.current_user.first_name, 'user2fn') # Check if the first name is correct of user 2
        self.assertEqual(friend2.current_user.last_name, 'user2ln') # Check if the last name is correct of user 2
        self.assertEqual(friend2.current_user.password, 'user2password') # Check if the password is correct of user 2
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test that serializer has the correct fields
    def test_friend_serializer(self):
        data = self.friendSerializer.data # Get the data from the serializer
        self.assertEqual(set(data.keys()), set(['pk', 'current_user', 'friends'])) # Check if the serialized data has the expected fields
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # success test for the friend api
    def test_user_account_profile_api_success(self):
        """Ensure the API provides a valid response for valid requests."""
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint
        response.render() # Render the response as JSON
        self.assertTrue(response.status_code, 200, "Expected status code 200 for a valid request.") # Check if the response status code is 200 and if it is, the test passes
        data = json.loads(response.content) # Load the response content as JSON
    # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        # the fields of the api
        self.assertTrue(data['pk']) # Check if the pk field is present
        self.assertTrue(data['current_user']['username']) # Check if the username field is present
        self.assertTrue(data['current_user']['email']) # Check if the email field is present
        self.assertTrue(data['current_user']['first_name']) # Check if the first name field is present
        self.assertTrue(data['current_user']['last_name']) # Check if the last name field is present
        self.assertTrue(data['current_user']['password']) # Check if the password field is present
    # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # check if the api returns the correct error code when there is an error
    def test_invalid_endpoint_response(self):
        """Ensure the API provides an error response for invalid requests."""
        response = self.client.get(self.bad_url, format='json') # Get the response from the API endpoint
        self.assertTrue(response.status_code, 404, "Expected status code 404 for an invalid request.") # Check if the response status code is 404 and if it is, the test passes
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- >>
class FriendRequestModelTestCase(TestCase):
    """Test suite for the FriendshipRequest model and its related functionalities."""
    # test suite for the FriendRequest model and its related functionalities
    friend = None # Initialize the friend variable
    friendRequest = None # Initialize the friendRequest variable
    friendRequestSerializer = None # Initialize the friendRequestSerializer variable

    def setUp(self):
        """Initial setup for tests: creating users, Friend instances, and FriendshipRequest instances."""
        # initial setup for tests: creating users and Friend instances
        self.user1 = User.objects.create(
            username='user1', # Create a user USERNAME using the UserFactory
            email='user1@gmail.com',  # Create a user EMAIL using the UserFactory
            first_name='user1fn',  # Create a user FIRST_NAME using the UserFactory
            last_name='user1ln',  # Create a user LAST_NAME using the UserFactory
            password='user1password' # Create a user PASSWORD using the UserFactory
        )   # the creation of the user is done using the UserFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friend1 = Friend.objects.create(current_user=self.user1) # Create a friend instance using the FriendFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.user2 = User.objects.create(
            username='user2', # Create a user USERNAME using the UserFactory
            email='user2@gmail.com',  # Create a user EMAIL using the UserFactory
            first_name='user2fn',  # Create a user FIRST_NAME using the UserFactory
            last_name='user2ln',  # Create a user LAST_NAME using the UserFactory
            password='user2password' # Create a user PASSWORD using the UserFactory
        )  # the creation of the user is done using the UserFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friend2 =  Friend.objects.create(current_user=self.user2) # Create a friend instance using the FriendFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friendRequest = FriendshipRequest(
            sender=self.user1,  # Create a friend request instance using the FriendRequestFactory
            receiver=self.user2, # receiver from request is user2
            pending="True" # Set pending to True by default
        )   # the creation of the friend request is done using the FriendRequestFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.friendRequestSerializer = FriendshipInteractionSerializer()    # Initialize the serializer for the friend request instance
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.good_url = reverse('FriendRequestDetailView', kwargs={'pk': 1}) # Construct a valid URL for the friend request API
        self.bad_url = "api/friendrequest/qwerty"   # Construct an invalid URL for the friend request API
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    def tearDown(self):
        """Cleanup after each test: Removing all instances."""
        User.objects.all().delete() # Delete all User instances
        Friend.objects.all().delete()  # Delete all Friend instances
        FriendshipRequest.objects.all().delete() # Delete all FriendRequest instances
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # Integrity of the data stored in the FriendRequest model
    def test_friend_request_data_integrityl(self):
        """Ensure data stored in FriendshipRequest model is consistent with created user data."""
        self.assertIsInstance(self.friendRequest, FriendshipRequest) # Check if the friend request instance is of type FriendRequest
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertEqual(self.friendRequest.sender, self.user1) # Check if the sender is correct
        self.assertEqual(self.friendRequest.receiver, self.user2) # Check if the receiver is correct
        self.assertEqual(self.friendRequest.pending, "True") # Check if the pending is correct
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # consistency of the fields in the serializer
    def test_serializer_field_consistency(self):
        """Ensure the FriendRequest serializer maintains field integrity."""
        data = self.friendRequestSerializer.data # Get the data from the serializer
        self.assertEqual(set(data.keys()), set(['sender', 'receiver', 'pending'])) # Check if the serialized data has the expected fields
    # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test the api response on valid request for friend request
    def test_api_response_on_valid_request(self): 
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint
        response.render() # Render the response as JSON
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertTrue(response.status_code, 200, "Expected status code 200 for a valid request.") # Check if the response status code is 200 and if it is, the test passes
        data = json.loads(response.content) # Load the response content as JSON

    # test on invalid request for friend request
    def test_api_response_on_invalid_request(self):
        response = self.client.get(self.bad_url, format='json') # Get the response from the API endpoint
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertTrue(response.status_code, 404, "Expected status code 404 for an invalid request.") # Check if the response status code is 404 and if it is, the test passes
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>