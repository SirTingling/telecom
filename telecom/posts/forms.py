# Import necessary Django modules
from django import forms # Importing the forms module from Django for form creation
from .models import UserArticle # Importing the UserArticle model from the models.py file in the same directory as this file

# Here, this is built on top of Django's ModelForm which automatically builds a form
# based on the given model's fields.
class UserPostForm(forms.ModelForm):
    
    # content field: 
    # Represents the main content of the user's post.
    # - It is required for form submission.
    # - It uses a Textarea widget for multi-line input with custom styling and attributes.
    # - Styling is done using CSS classes and inline styles.
    content = forms.CharField(
        required=True, 
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Bootstrap class for styling the textarea
            'placeholder': 'random text to fill as placeholder',  # Placeholder text when the textarea is empty
            'style': 'min-width: 100%',  # Ensures the textarea takes up the full width of its container
            'rows': '10'  # Defines the number of visible rows in the textarea
        })
    )
    
    # content_image field: 
    # Allows users to upload an image as part of their post.
    # - It is optional, so it's not required for form submission.
    # - Uses the FileInput widget with custom styling and attributes.
    # - It has an associated JavaScript function (`addImage`) that is triggered on file input changes.
    content_image = forms.ImageField(
        label="Image",  # The label displayed next to the input field in the form
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file',  # Bootstrap class for styling the file input
            'id': 'postImage',  # Unique ID for the input field, useful for targeting with JavaScript or CSS
            'oninput': 'addImage(this)'  # Calls the `addImage` JavaScript function when the input changes
        })
    )
    
    # Here specifies which model the form is tied to and which fields from that model
    # should be included in the form.
    class Meta:
        model = UserArticle  # The model that this form is based on
        fields = ['content', 'content_image']  # The model fields to include in the form
