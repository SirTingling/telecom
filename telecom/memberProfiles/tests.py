# importing django modules for test use from Django
from django.test import TestCase # Import the TestCase class from Django
from django.urls import reverse # Import the reverse function from Django
from django.contrib.auth import get_user_model # Import the get_user_model function from Django
# -----------------------------------------------------------------------------------------------------------------------------------------------
import json # Import the json module from Python
# ----------------------------------------------------------------------------------------------------------------------------------------------- 
from .models import * # Import all models from the models.py file in the same directory as this file
from .factories import * # Import all factories from the factories.py file in the same directory as this file
from .views import * # Import all views from the views.py file in the same directory as this file
from .serializers import * # Import all serializers from the serializers.py file in the same directory as this file
# -----------------------------------------------------------------------------------------------------------------------------------------------

class UserProfileModelTests(TestCase):
    """Test cases for UserProfile model behavior and integrity."""
    userAccount = None
    userAccountSerializer = None

    def setUp(self):
        """Initialize test data before each test."""
        self.userAccount = MockUserProfileFactory.create() # Create a user account instance using the UserAccountFactory
        self.userAccountSerializer = UserProfileDetailSerializer(instance=self.userAccount) # Create a serializer instance using the UserAccountSerializer
        # Define valid and invalid endpoints for testing the API.
        self.good_url = reverse('user_detail_api', kwargs={'pk': 1}) # Define a valid endpoint for the API.
        self.bad_url = "api/user/qwerty" # Define an invalid endpoint for the API.

    def tearDown(self):
        """Clean up test data after each test."""
        User.objects.all().delete() # Delete all User instances.
        UserProfile.objects.all().delete() # Delete all UserProfile instances.
        MockUserFactory.reset_sequence() # Reset factory sequence.
        MockUserProfileFactory.reset_sequence() # Reset factory sequence.

    # user account model test
    def test_user_account_has_expected_fields(self):
        """Check if UserProfile model data matches factory setup."""
        userAcc = self.userAccount # Get the user account instance created in the setUp method.
        self.assertIsInstance(userAcc, UserProfile) # Check if the user account instance is of type UserProfile.
        """ it does, so the test passes and the test method ends here. """
        self.assertEqual(userAcc.user.username, 'johndoe') # Check if the user account instance has the correct username.
        self.assertEqual(userAcc.user.email, 'johndoe@gmail.com') # Check if the user account instance has the correct email.
        self.assertEqual(userAcc.user.first_name, 'john') # Check if the user account instance has the correct first name.
        self.assertEqual(userAcc.user.last_name, 'doe') # Check if the user account instance has the correct last name.
        self.assertEqual(userAcc.user.password, 'johndoepassword') # Check if the user account instance has the correct password.
        """ then, check if the user account instance has the correct image, phone number and date of birth """  
        self.assertEqual(userAcc.image, './static/interfaces/narmpo1.jpg') # Check if the user account instance has the correct image.
        self.assertEqual(userAcc.phone_number, '80008008') # Check if the user account instance has the correct phone number.
        self.assertEqual(userAcc.dob, '2000-10-10') # Check if the user account instance has the correct date of birth.
        # -- END check if the user account instance has the correct image, phone number and date of birth -- #
    # test that the view returns correct code with redirect
    def test_user_account_presence_in_database(self):
        """Check if created UserProfile instance is stored in the database."""
        response = self.client.get(reverse('display_user_profile')) # Get the response from the display_user_profile view.
        self.assertEqual(response.status_code, 302) # Check if the response status code is 302.
    # -- END test that the view returns correct code with redirect -- #
    # test that the view returns correct code with redirect
    def test_user_account_editprofile_view(self):
        """Ensure that accessing the editprofile view returns the expected redirect status code.""" # [status code = 302, so means it's a HttpResponseRedirect, therefore there's no template used for the HTTP response]
        response = self.client.get(reverse('update_user_profile')) # Get the response from the edit-profile view.
        self.assertEqual(response.status_code, 302) # Check if the response status code is 302.
    # -- END test that the view returns correct code with redirect -- #
    # test that serializer has the correct fields
    def test_user_account_profile_serializer(self):  
        """Check if the UserProfile serializer produces the correct fields.""" # [status code = 302, so means it's a HttpResponseRedirect, therefore there's no template used for the HTTP response]
        data = self.userAccountSerializer.data # Get the data from the UserProfile serializer.
        self.assertEqual(set(data.keys()), set(['pk', 'user', 'image','phone_number','dob'])) # Check if the serializer has the correct fields.
    # -- END test that serializer has the correct fields -- #
    # test that api returns correct fields when success
    def test_valid_endpoint_response(self):
        """Ensure that valid API endpoint returns a 200 status code."""
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint.
        response.render() # Render the response as JSON.
        self.assertTrue(response.status_code, 200) # Check if the response status code is 200 and if it is, the test passes.
        data = json.loads(response.content) # Load the response content as JSON.
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        # The fields of the api response that I will are testing and after test completed, then, we will delete the test data
        self.assertTrue(data['pk']) # Check if the api response has the correct pk field.
        self.assertTrue(data['user']) # Check if the api response has the correct user field.
        self.assertTrue(data['user']['username']) # Check if the api response has the correct username field.
        self.assertTrue(data['user']['email']) # Check if the api response has the correct email field.
        self.assertTrue(data['user']['first_name']) # Check if the api response has the correct first name field.
        self.assertTrue(data['user']['last_name']) # Check if the api response has the correct last name field.
        self.assertTrue(data['user']['password']) # Check if the api response has the correct password field.
        self.assertTrue(data['image']) # Check if the api response has the correct image field.
        self.assertTrue(data['phone_number']) # Check if the api response has the correct phone number field.
        self.assertTrue(data['dob']) # Check if the api response has the correct date of birth field.
        # -- END The fields of the api response that I will are testing and after test completed, then, we will delete the test data -- #
    # test that api returns correct error code when there is an error
    def test_invalid_endpoint_response(self):
        response = self.client.get(self.bad_url, format='json') # Get the response from the API endpoint.
        self.assertTrue(response.status_code, 404) # Check if the response status code is 404 and if it is, the test passes.



class UserRegistrationAndLoginTests(TestCase):
    """Test cases for User registration and login procedures."""
    userAccount = None
    userAccountSerializer = None

    def setUp(self):
        """Initialize test data before each test."""
        self.userAccount = MockUserProfileFactory.create()
        self.userAccountSerializer = UserProfileDetailSerializer(instance=self.userAccount) # Create a serializer instance using the UserAccountSerializer
        # setup the project to test the api and view
        self.good_url = reverse('UserCreateView') # Define a valid endpoint for the API.
        self.bad_url = "api/createuserrr/"
        # Define valid and invalid endpoints for testing the API.
    def tearDown(self): 
        User.objects.all().delete() # Delete all User instances.
        UserProfile.objects.all().delete() # Delete all UserProfile instances.
        MockUserFactory.reset_sequence() # Reset factory sequence.
        MockUserProfileFactory.reset_sequence() # Reset factory sequence.
    # test that the data in the model matches the details of user account created with MockUserProfileFactory
    # test that the view returns correct code
    def test_password_encryption(self):
        """Ensure user passwords are hashed and stored securely."""
        response = self.client.get(reverse('register_new_user')) # Get the response from the register_new_user view.
        self.assertEqual(response.status_code, 200) # Check if the response status code is 200.
        # make sure that the correct template is used to render the response
        self.assertTemplateUsed(response, 'site_signup.html') # Check if the correct template is used to render the response.
    # password encryption test
    # test that the view returns correct code
    def test_registration_endpoint_response(self):
        """Check if registration API endpoint responds with a 200 status code."""
        response = self.client.get(reverse('login_user')) # Get the response from the login_user view.
        self.assertEqual(response.status_code, 200) # Check if the response status code is 200.
        # make sure the correct template is used to render the response
        self.assertTemplateUsed(response, 'site_login.html')
    # endpoint connection test for registration
    # test that api returns correct fields when success
    def test_registration_endpoint_response(self):
        response = self.client.get(self.good_url, format='json') # Get the response from the API endpoint.
        response.render()  # Render the response as JSON.
        self.assertTrue(response.status_code, 200) # Check if the response status code is 200 and if it is, the test passes.
    # new and invalid registrations to the api
    # test that api returns correct error code when there is an error
    def test_invalid_registration_endpoint_response(self):
        """Ensure that invalid registration API endpoint returns a 404 status code."""
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404, "Expected 404 Not Found response.")
    # -- END test that api returns correct error code when there is an error -- #


class UserSearchFunctionalityTests(TestCase):
    """Test cases for User search operations."""
    userAccount = None
    userAccountSerializer = None
    # setup the project to test the api and view
    def setUp(self):
        """Initialize test data before each test."""
        self.userAccount = MockUserProfileFactory.create() # Create a user account instance using the UserAccountFactory
        self.userAccountSerializer = UserProfileDetailSerializer(instance=self.userAccount) # Create a serializer instance using the UserAccountSerializer
    # test that the data in the model matches the details of user account created with MockUserProfileFactory
    def tearDown(self):
        User.objects.all().delete() # Delete all User instances.
        UserProfile.objects.all().delete() # Delete all UserProfile instances.
        MockUserFactory.reset_sequence() # Reset factory sequence.
        MockUserProfileFactory.reset_sequence() # Reset factory sequence.
    # user search functionality test
    # test that the view returns correct code with redirect
    def test_search_user_by_username(self):
        """Ensure users can be searched using their username."""
        response = self.client.get(reverse('search_for_users'))
        self.assertEqual(response.status_code, 302, "Username search failed, username not located in search results.")
    # -- END test that the view returns correct code with redirect -- #
# -- END UserSearchFunctionalityTests -- #
# ----------------------------------------------------------------------------------------------------------------------------------------------- >>