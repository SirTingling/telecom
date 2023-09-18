from django.db import models
from django.contrib.auth.models import User

# User Profile Model:
# This model represents additional information about a user beyond what the default Django User model provides.
class UserProfile(models.Model):
    """
    Extended user profile to store additional user-related information.
    - image: Profile picture of the user.
    - phone_number: User's contact number.
    - dob: Date of birth of the user.–-
    """
    
    # Link the UserProfile to the Django built-in User model.
    user = models.OneToOneField(
        User, 
        related_name='profile', 
        on_delete=models.CASCADE, 
        verbose_name="User"
    )
    
    # User's profile picture. Default image will be used if no image is provided.
    image = models.ImageField(
        default='media/profileImage/male-user.png',
        upload_to='profileImage/',  # renamed to a more standard naming convention
        null=True, 
        blank=True, 
        verbose_name="Profile Image"
    )
    
    # Unique contact number for the user.
    phone_number = models.CharField(
        max_length=20,
        null=True, 
        blank=True, 
        unique=True,
        verbose_name="Phone Number"
    )
    
    # User's date of birth.
    dob = models.DateField(
        null=True, 
        blank=True, 
        verbose_name="Date of Birth"
    )

    # Return the username when the UserProfile object is printed.
    def __str__(self):
        return self.user.username
