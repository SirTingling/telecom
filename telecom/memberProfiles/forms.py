# imports for the form classes
from django import forms # django forms imports
from django.forms import (
    ModelForm,  # django model form imports
    TextInput,  # django text input widget import
    EmailInput,  # django email input widget import
    PasswordInput,  # django password input widget import
    FileInput,  # django file input widget import
    DateInput # django date input widget import
)
# -----------------------------------------------------------------------------------------------------------------------------------------------
from .models import UserProfile # Import the UserProfile model from the models.py file in the same directory as this file
from django.contrib.auth.models import User # django auth models imports
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Registration form for the Django User model
class RegistrationUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': TextInput(attrs={
                'id': "username",
                'class': "form-control",
                'placeholder': 'Username (e.g., john_doe)',
            }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'First Name (e.g., John)',
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Last Name (e.g., Doe)',
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email Address (e.g., john.doe@example.com)',
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Choose a secure password',
            }),
        }

# Form to capture additional fields related to the User profile
class RegistrationUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('image', 'phone_number', 'dob')
        # Placeholders are typically added for input fields
        # However, for 'image' since it's a FileInput, it doesn't usually need a placeholder

# Form for updating the built-in Django User model fields
class UpdateUserForm(forms.ModelForm):

    # Define fields with specific requirements or custom widgets
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Update your username'
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Update your first name'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Update your last name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Update your email address'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# Form for updating the additional fields associated with the User profile
class UpdateUserProfileForm(forms.ModelForm):

    image = forms.ImageField(
        widget=FileInput(attrs={'class': 'form-control-file'})
        # No placeholder for FileInput, but can add 'help_text' if needed for guidance
    )
    phone_number = forms.IntegerField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Update your phone number (e.g., +1234567890)'
        })
    )
    dob = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'Update your birthdate (e.g., YYYY-MM-DD)'
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = ['image', 'phone_number', 'dob']
