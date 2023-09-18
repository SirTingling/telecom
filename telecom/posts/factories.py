# -------------------------------------------------------------------------------------------------------------------------------------------- >>
import factory # import factory components
import random # import random for generating random data
from datetime import datetime, timedelta # import datetime for generating timestamps
from .models import UserArticle # import the UserArticle model
from memberProfiles.factories import MockUserFactory # import the MockUserFactory from the memberProfiles app
# -------------------------------------------------------------------------------------------------------------------------------------------- >>
# Define a factory for creating test UserArticle instances
class UserPostTestFactory(factory.django.DjangoModelFactory):
    
    # Link to the user factory to create a related user instance
    user = factory.SubFactory(MockUserFactory)
    
    # Generate randomized content for the post using Faker
    content = factory.Faker('sentence', nb_words=10)
    
    # Option to select a random image from a predefined list of test images
    content_image = factory.LazyAttribute(lambda _: random.choice([
        "./media/profileImage/lampo1.jpg",
        "./static/interfaces/narmpo1.jpg",
    ]))
    
    # Generate a random timestamp within the last 30 days for varied testing
    timestamp = factory.LazyAttribute(lambda _: datetime.now() - timedelta(days=random.randint(0, 30)))

    # Meta class provides configurations for the factory
    class Meta:
        model = UserArticle
