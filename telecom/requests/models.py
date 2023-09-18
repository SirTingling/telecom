# import models from django
from django.db import models # Import the models module from Django
from memberProfiles.models import * # Import all models from the memberProfiles app
from django.core.exceptions import ObjectDoesNotExist # Importing the ObjectDoesNotExist exception from Django
# ---------------------------------------------------------------------------------------------------------------------- >>
# User Profile model extended from Django User model
# ---------------------------------------------------------------------------------------------------------------------- >>
class Friend(models.Model):
    current_user = models.OneToOneField(User,related_name='current_user', on_delete=models.CASCADE, null=True) # A one-to-one relationship to the User model
    friends = models.ManyToManyField(User, related_name='friends', blank=True) # A many-to-many relationship to the User model

    def __str__(self):
        return self.current_user.username # Return the username of the current user

    def add_friend(self, to_be_added):
        # if to_be_added is not in friend list, add account as friend
        if not to_be_added in self.friends.all():
            self.friends.add(to_be_added) # Add the friend to the friend list
            self.save() # Save the changes to the database
 
    def remove_friend(self, to_be_removed):
        # if to_be_removed is in friend list, remove account as friend
        if to_be_removed in self.friends.all():
            self.friends.remove(to_be_removed) # Remove the friend from the friend list
            self.save() # Save the changes to the database

    def unfriend(self, user_to_remove):
        # remove account from user's friend list
        self.remove_friend(user_to_remove)

        # remove user from friend's friend list
        friends_list = Friend.objects.get(current_user=user_to_remove) # Get the friend's friend list
        friends_list.remove_friend(self.current_user) # Remove the current user from the friend's friend list

# ---------------------------------------------------------------------------------------------------------------------- >>
# FriendshipRequest Model: Represents a friend request sent from one user to another.
class FriendshipRequest(models.Model):
    """
    FriendshipRequest Model: 
    Represents a friend request sent from one user to another.
    """
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender') # A foreign key to the User model
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'receiver') # A foreign key to the User model
    pending = models.BooleanField(blank = True, null = False, default = True) # Set pending to True by default
    timestamp = models.DateTimeField(auto_now_add = True) # Set the timestamp to the current time when a request is created
    
    def __str__(self):
        """Return a string representation of the request, displaying sender and receiver."""
        return f"Request from {self.sender.username} to {self.receiver.username}"

    # add sender to reciever's friend list, add reciever to sender's friend list,
    def approve_request(self):
        """
        Approve a friend request, establishing a mutual friendship between the sender and receiver.
        """
        # get the user that recieved the friend request
        recieved = Friend.objects.get(current_user=self.receiver)

        # if recieved friend request
        if recieved:
            # call add_friend function sender [sender adds receiver]
            recieved.add_friend(self.sender)

            # get the user that send the friend request
            send = Friend.objects.get(current_user=self.sender)
            
            # call add_friend function on receiver [receiver adds sender]
            send.add_friend(self.receiver)

            # Mark the request as approved by setting 'pending' to False
            self.pending = False # Set pending to False to ensure it's no longer in a pending state
            self.save() # Save the changes to the database
        
        if ObjectDoesNotExist:
            # Handle error gracefully
            print(f"Error: profile was not found, thus friendship termination failed.")
    
    # set the pending state for the friend request to False
    def reject_request(self):
        # make pending false when user rejected friend request
        """
        Reject a friend request, ensuring it's no longer in a pending state.
        """
        self.pending = False # Set pending to False to ensure it's no longer in a pending state
        self.save() # Save the changes to the database

    # retract sent friend request
    def retract_request(self):
        # make request_state false when user retractedfriend request
        """
        Withdraw a previously sent friend request.
        """
        self.pending = False # Set pending to False to ensure it's no longer in a pending state
        self.save() # Save the changes to the database