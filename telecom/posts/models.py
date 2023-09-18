# importing the User model from Django's built-in authentication system.
# ---------------------------------------------------------------------------------------------------------------------- >>
from django.db import models # Import the models module from Django
from memberProfiles.models import *  # Import all models from the memberProfiles app
# ---------------------------------------------------------------------------------------------------------------------- >> 

# Represents individual posts made by users.
class UserArticle(models.Model):
    
    # The main textual content of the user's post.
    # Given the possible size of a post, CharField is used with a large max_length.
    content = models.TextField()

    # Image associated with the post.
    # 'upload_to' defines the subdirectory within MEDIA_ROOT where this image is stored.
    # 'null=True' and 'blank=True' indicate that the image is optional.
    content_image = models.ImageField(upload_to='postImage', null=True, blank=True)

    # The date and time when the post was created or last modified.
    # 'auto_now=True' means that every time the post is saved, this field will be updated.
    timestamp = models.DateTimeField(auto_now=True)

    # A foreign key to the User model.
    # this post will be deleted as well.
    # 'related_name' defines the reverse relation from User to UserPost,
    # 'u.user_posts.all()' will give you all posts associated with this user.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    # String representation of the model for better readability in Django's admin and elsewhere.
    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}..."  # Display username and first 50 chars of content

