# django db models bigauto field imports
from django.db import models # django db models imports
from django.contrib.auth.models import User # django auth models imports

# Chatroom_identifier Model
# Represents a distinct chat room where multiple users can communicate.

class Interface(models.Model):
    # The unique name assigned to a chat room.
    chatroom = models.CharField(max_length=255, unique=True, blank=False)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.chatroom


class InterfaceContent(models.Model):
    # stores the message content
    content = models.CharField(max_length=10000)

    # stores the message sent time
    timestamp = models.DateTimeField(auto_now=True)

    # stores the post's user, this field is a fk that links to the django User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatroom_user")

    # stores the chatroom name, this field is a fk that links to the Chatroom model
    chatroom = models.ForeignKey(Interface, on_delete=models.CASCADE,)

    def __str__(self):
        return self.content
    