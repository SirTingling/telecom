# imports of django form classes
from django import forms # imports of django form classes
from .models import Interface # imports of django classroom identifier model

# Chatroom_identifierForm
# A form that facilitates the creation and management of chat rooms.
class ChatRoomCreationForm(forms.ModelForm):

    # Field for entering the name of the chat room.
    # The widget customizes its appearance and behavior in the HTML form.
    chatroom = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-2',  # Added margin-top for spacing
                'placeholder': 'Chatroom Name', # Placeholder text for user guidance
                'aria-label': 'Chatroom Name',  # For accessibility
                'aria-describedby': 'chatroom-name-help',  # Linking with help text
            }
        ),
        help_text="Enter a unique name for the chatroom.",  # Help text for user guidance
        label="Create a new chatroom", # Custom label for the field
        error_messages={
            'required': 'The Chatroom name is required.'  # Custom error message for missing value
        }
    )
    # ----------------------------------------------------------------------------------------------------------------------------------

    class Meta:
        # Specifies that this form is linked with the ChatRoom model.
        model = Interface
        
        # Declares that the only field to be used from the model in this form is 'chatroom'.
        fields = ['chatroom']
