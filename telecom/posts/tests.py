# DJANGO REST FRAMEWORK IMPORT STATEMENTS
from django.test import TestCase # Django's TestCase class for unit testing
from django.urls import reverse # Django's reverse function for URL lookups
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
import json
from .models import * # Import all models from the models.py file in the same directory as this file
from .factories import * # Import all factories from the factories.py file in the same directory as this file
from .views import * # Import all views from the views.py file in the same directory as this file
from .serializers import * # Import all serializers from the serializers.py file in the same directory as this file
from memberProfiles.factories import * # Import all factories from the factories.py file in the same directory as this file
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# User Model Test Case for testing the User model
class UserPostTestCase(TestCase):
    """ https://docs.djangoproject.com/en/3.1/topics/testing/overview/ """
    """ setting up the environment for each test """
    userPost = None
    userPostSerializer = None
    good_url = None
    bad_url = None

    def setUp(self):
        """
        This method sets up the environment for each test. Here, a dummy user post is created,
        its serializer is initialized, and valid and invalid URLs for testing are constructed.
        """
        # Create a more realistic user post using the factory
        self.userPost = UserPostTestFactory.create() # Create a user post instance using the UserPostTestFactory
        self.userPostSerializer = UserPostDetailSerializer(instance=self.userPost) # Initialize the serializer for the user post instance
        # Define valid and invalid endpoints for testing the API. 
        self.good_url = reverse('api_user_post_retrieve', kwargs={'pk': 1}) # Construct a valid URL for the user post API
        self.bad_url = "api/userpost/qwerty" # Construct an invalid URL for the user post API
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    def tearDown(self):
        """
        This method cleans up the environment after each test. All created objects are deleted,
        and sequences in factories are reset.
        """
        # Clean up the created objects to maintain isolation between tests
        User.objects.all().delete() # Delete all User instances
        UserProfile.objects.all().delete() # Delete all UserProfile instances
        UserArticle.objects.all().delete() # Delete all UserArticle instances
        MockUserFactory.reset_sequence() # Reset the sequence in the MockUserFactory
        MockUserProfileFactory.reset_sequence() # Reset the sequence in the MockUserProfileFactory
        UserPostTestFactory.reset_sequence() # Reset the sequence in the UserPostTestFactory
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test the data in the model matches the details of user account created with MockUserFactory
    def test_user_post_factory(self):
        """
        Test if the UserPost created by the factory matches the specified attributes.
        """
        # Reset factory sequences to ensure consistent data across tests
        userPost = self.userPost # Get the user post instance created in the setUp method
        self.assertIsInstance(userPost, UserArticle) # Check if the user post instance is of type UserArticle
        # Check if the user post instance is of type UserArticle 
        self.assertEqual(userPost.user.username, 'john_doe') # Check if the username is correct
        self.assertEqual(userPost.user.email, 'john.doe@example.com') # Check if the email is correct
        self.assertEqual(userPost.user.first_name, 'John') # Check if the first name is correct
        self.assertEqual(userPost.user.last_name, 'Doe') # Check if the last name is correct
        self.assertEqual(userPost.user.password, 'securepassword123') # Check if the password is correct
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertEqual(userPost.content, 'This is a sample post content for testing purposes.') # Check if the content is correct
        self.assertEqual(userPost.content_image, './static/interfaces/narmpo1.jpg') # Check if the content image is correct
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test that serializer has the correct fields
    def test_posts_view_redirection(self):
        """
        Ensure that accessing the 'posts' view results in an expected redirection.
        """
        response = self.client.get(reverse('home')) # Get the response from accessing the 'posts' view
        self.assertEqual(response.status_code, 302) # Check if the response status code is 302 and if it is, the test passes
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test that serializer has the correct fields
    def test_user_post_serializer_fields(self):
        """
        Validate that the serializer correctly serializes the expected fields.
        """
        data = self.userPostSerializer.data # Get the serialized data from the serializer
        self.assertEqual(set(data.keys()), set(['pk', 'user', 'content','content_image','timestamp'])) # Check if the serialized data has the expected fields
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test that api returns correct fields when success
    def test_api_retrieval_success(self):
        """
        Confirm that the API returns the expected fields and values when provided with a valid endpoint.
        """
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint
        response.render() # Render the response as JSON
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        self.assertTrue(response.status_code, 200) # Check if the response status code is 200 and if it is, the test passes
        data = json.loads(response.content) # Load the response content as JSON
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
        # fields for the api to process and return
        self.assertTrue(data['pk']) # Check if the response has the 'pk' field
        self.assertTrue(data['user']) # Check if the response has the 'user' field
        self.assertTrue(data['user']['username']) # Check if the response has the 'username' field
        self.assertTrue(data['user']['email']) # Check if the response has the 'email' field
        self.assertTrue(data['user']['first_name']) # Check if the response has the 'first_name' field
        self.assertTrue(data['user']['last_name']) # Check if the response has the 'last_name' field
        self.assertTrue(data['user']['password']) # Check if the response has the 'password' field
        self.assertTrue(data['content'])    # Check if the response has the 'content' field
        self.assertTrue(data['content_image']) # Check if the response has the 'content_image' field
        self.assertTrue(data['timestamp']) # Check if the response has the 'timestamp' field
        # -------------------------------------------------------------------------------------------------------------------------------------------- >>
    # test the api returns correct fields when error
    def test_post_api_error(self):
        """
        Confirm that accessing an invalid API endpoint returns a 404 status code.
        """
        # response would be 404 if the url is invalid
        response = self.client.get(self.bad_url, format='json') # Get the response from the API endpoint
        self.assertTrue(response.status_code, 404) # Check if the response status code is 404 and if it is, the test passes
    # -------------------------------------------------------------------------------------------------------------------------------------------- >>
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>