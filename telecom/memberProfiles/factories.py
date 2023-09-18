# factory import components to create mock objects for testing purposes.
import factory # FactoryBoy
from .models import User, UserProfile # Import the User and UserProfile models from the models.py file in the same directory as this file

# Factory for creating mock User objects
class MockUserFactory(factory.django.DjangoModelFactory):
    """
    Factory for generating mock User instances for testing purposes.
    """

    # Setting default values for the User fields
    username = factory.Sequence(lambda n: f'testuser{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@gmail.com')
    first_name = 'Test'
    last_name = 'User'
    password = factory.PostGenerationMethodCall('set_password', 'testuserpassword')

    class Meta:
        model = User


# Factory for creating mock UserProfile objects
class MockUserProfileFactory(factory.django.DjangoModelFactory):
    """
    Factory for generating mock UserProfile instances for testing purposes.
    """

    # Linking the UserProfileFactory to the UserFactory
    user = factory.SubFactory(MockUserFactory)

    # Setting default values for the UserProfile fields
    image = "./static/interfaces/narmpo1.jpg"
    phone_number = factory.Sequence(lambda n: f'8000{n}400{n}')  # Example: 8000104001, 8000208002, etc.
    dob = "2000-06-11"

    class Meta:
        model = UserProfile
