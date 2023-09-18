# django imports for the requests app
from django.contrib import messages # Importing the messages module from Django
from django.http import HttpResponse # Importing the HttpResponse class from Django
from django.shortcuts import render, redirect # Importing the render and redirect functions from Django
# ----------------------------------------------------------------------------------------------------------------------------------- >>
from .models import * # Importing all models from the requests app
# ----------------------------------------------------------------------------------------------------------------------------------- >>
from memberProfiles.models import * # Importing the UserAccount model from the memberProfiles app
from memberProfiles.forms import * # Importing all models from the memberProfiles app
from posts.models import * # Importing the UserArticle model from the posts app
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# function used to check if there are any friend requests
def has_pending_friend_request(sender, receiver):
    """
    Check for a pending friend request between two users.

    Args:
    - sender (User): The user who sent the friend request.
    - receiver (User): The user who received the friend request.

    Returns:
    - FriendshipRequest instance if exists; None otherwise.
    """

    try:
        return FriendshipRequest.objects.get(sender=sender, receiver=receiver, pending=True)
    except FriendshipRequest.DoesNotExist:
        return False


def friendDetail(request, username):
    """
    Render a detailed view of a specific friend's profile, along with associated details like posts, mutual friends, etc.

    Args:
    - request (HttpRequest): Standard Django request object.
    - username (str): The username of the friend to be viewed.

    Returns:
    - Rendered HTML page containing the friend's details.
    """
    context = {}
    user = request.user
    # Ensure the user is authenticated before proceeding
    if user.is_authenticated:
        # console.log("User is authenticated successfully")
        if request.method == "GET":
            
            viewed_user = User.objects.get(username = username)
            profile = UserProfile.objects.get(user = viewed_user)
            profile_form = RegistrationUserProfileForm(instance=user.profile)
            posts = UserArticle.objects.filter(user=viewed_user)
            # Fetching the user whose details are to be viewed
            try:
                # get the friends of the viewed user
                friend = Friend.objects.get(current_user=viewed_user)
            except Friend.DoesNotExist:
                messages.error(request, f"User {username} does not exist.")
                friend = Friend(current_user=viewed_user)
                friend.save()

            # save friend list data of viewed user in context
            friend_list = friend.friends.all()
            context['friend_list'] = friend_list

            # filter UserAccount based on if user is in the friend_list
            # this is the get the profile image of friends
            friend_profile = UserProfile.objects.filter(user__in=friend_list)
            context['friend_profile'] = friend_profile

            is_self = False
            is_friend = False
            # 0 - no request, 1 - request to user, 2 - request from user
            request_status = 0

            # check if user is friends with viewed user
            if friend_list.filter(pk=user.id):
                is_friend = True
            else:
                is_friend = False
                # if there is a friend request from viewed user to current user
                if has_pending_friend_request(sender = viewed_user, receiver = user) != False:
                    # set request_state to 1 [there is a request to user]
                    request_status = 1
                    # get the specific id from the friendRequest model, save in context
                    context['req_id'] = has_pending_friend_request(sender = viewed_user, receiver = user).id
                # if there is a friend request from current user to viewed user
                elif has_pending_friend_request(sender = user, receiver = viewed_user) != False:
                    # set request_state to 2 [there is a request from user]
                    request_status = 2
                else:
                    # set request_state to 0 [there is no user]
                    request_status = 0

            # save data in context
            context['is_self'] = is_self
            context['is_friend'] = is_friend
            context['request_status'] = request_status
            
            context['user'] = viewed_user
            context['profile'] = profile
            context['profile_form'] = profile_form
            context['posts'] = posts

    else:
        messages.error(request, 'Login first before viewing profile')
        return redirect('login_user')

    return render (request, 'friendrequests.html', context)



def initiate_friend_request(request):
    """
    Handle the initiation of a new friend request from the current user to another user.

    Args:
    - request (HttpRequest): Standard Django request object containing friend request details.

    Returns:
    - HttpResponse indicating the result of the friend request initiation.
    """
    currentUser = request.user

    if request.method == "POST" and currentUser.is_authenticated:
        # get user_id of reciever
        user_id = request.POST.get("receiverID")

        # if there user_id exists
        if user_id:
            # set reciever of the friend request to be the User with the user_id
            receiver = User.objects.get(pk=user_id)

            # check if there is any friend request from currentUser to receiver
            try:
                friend_requests = FriendshipRequest.objects.filter(sender=currentUser, receiver=receiver)

                try:
                    for req in friend_requests:
                        # if the request is still active (pending)
                        if req.pending:
                            messages.info(request, "There is a pending friend request to this user")
                    # send friend request
                    friend_request = FriendshipRequest(sender=currentUser, receiver=receiver)
                    friend_request.save()
                    messages.success(request, "Friend request successfully send")

                except Exception as e:
                    messages.error(request, "There is a error when sending friend request to this user")

            # if there is no friend request from current user to ANY user
            except FriendshipRequest.DoesNotExist:
                # send friend request
                friend_request = FriendshipRequest(sender=currentUser, receiver=receiver)
                friend_request.save()
                messages.success(request, "Friend request successfully send")

        # if no user_id
        else:
            messages.error(request, "User does not exist")
    return HttpResponse



def handle_friend_request(request):
    """
    General function to handle friend request operations: approve, decline, or withdraw.

    Args:
    - request (HttpRequest): The standard Django request object containing friend request details.

    Returns:
    - HttpResponse: Indicates the result of the action taken.
    """
    currentUser = request.user

    # Check if the request method is POST and the user is authenticated
    if request.method == "POST" and currentUser.is_authenticated:
        # Get the user_id of the receiver from the POST data
        user_id = request.POST.get("receiverID")

        # If a user_id exists
        if user_id:
            # Set the receiver of the friend request to be the User with the specified user_id
            receiver = User.objects.get(pk=user_id)

            # Check if there is any pending friend request from currentUser to receiver
            try:
                # Get the request that was sent
                reqToCancel = FriendshipRequest.objects.filter(sender=currentUser, receiver=receiver, pending=True)

                # There might be previous requests between the two users, so get the latest one and cancel it
                reqToCancel.first().cancel()
                messages.success(request, "Friend request has been cancelled")
            
            except Exception as e:
                # Return an error message if there's no friend request sent to this user
                messages.error(request, "An error has occurred, there is no friend request sent to this user")

        # If no user_id is provided
        else:
            messages.error(request, "User does not exist")

    # Return an HttpResponse
    return HttpResponse




def unfriend(request):
    """
    Handle the removal of a user from the friend list of the current user.

    Args:
    - request (HttpRequest): The standard Django request object containing the ID of the friend to be removed.

    Returns:
    - HttpResponse: Indicates the result of the unfriend operation.
    """
    currentUser = request.user
    
    # Check if the request method is POST and the user is authenticated
    if request.method == "POST" and currentUser.is_authenticated:
        # Get the user_id of the receiver from the POST data
        user_id = request.POST.get("receiverID")

        # If user_id exists
        if user_id:
            try:
                # Get the FriendToRemove (using the user_id) from the User model
                FriendToRemove = User.objects.get(pk=user_id)

                # Get the FriendToRemove from the Friend model and call the unfriend method 
                # to remove the friend from the authenticated user's own friend list
                self_friend_list = Friend.objects.get(current_user=currentUser)
                self_friend_list.unfriend(FriendToRemove)
                
                messages.success(request, FriendToRemove.username + " has been removed from the friend list")
                messages.success(request, "Friend request declined.")
            except Exception as e:
                # Return an error message if an issue occurs
                messages.error(request, "An error has occurred")
        else:
            messages.error(request, "Friend does not exist")

    # Return an HttpResponse
    return HttpResponse




def approve_friend_request(request, *args, **kwargs):
    """
    Approve a pending friend request.

    Args:
    - request (HttpRequest): The HTTP request object.
    - req_id (int): ID of the friend request to be approved.

    Returns:
    - HttpResponse: Indicates the outcome of the operation.
    """
    currentUser = request.user

    # Check if the request method is GET and the user is authenticated
    if request.method == "GET" and currentUser.is_authenticated:

        # Get the id of the friend request from kwargs
        req_id = kwargs.get("req_id")

        # If req_id exists
        if req_id:
            # Get the friend_request object based on the req_id
            friend_request = FriendshipRequest.objects.get(pk=req_id)

            try:
                # Call the accept method on the friend_request object
                friend_request.accept()
                messages.success(request, "Friend request has been accepted")

            except Exception as e:
                # Return an error message if there's an issue when accepting the friend request
                messages.error(request, "An error has occurred when accepting the friend request")
            except FriendshipRequest.DoesNotExist:
                messages.error(request, "Friend request not found.")
        else:
            messages.error(request, "Request does not exist")

    # Return an HttpResponse
    return HttpResponse




def reject_friend_request(request, *args, **kwargs):
    """
    Decline a pending friend request.

    Args:
    - request (HttpRequest): The HTTP request object.
    - req_id (int): ID of the friend request to be declined.

    Returns:
    - HttpResponse: Indicates the outcome of the operation.
    """
    currentUser = request.user
    
    # Check if the request method is GET and the user is authenticated
    if request.method == "GET" and currentUser.is_authenticated:

        # Get the id of the friend request from kwargs
        req_id = kwargs.get("req_id")

        # If req_id exists
        if req_id:
            # Get the friend_request object based on the req_id
            friend_request = FriendshipRequest.objects.get(pk=req_id)

            try:
                # Call the decline method on the friend_request object
                friend_request.decline()
                messages.success(request, "Friend request has been declined")
            except Exception as e:
                # Return an error message if there's an issue when declining the friend request
                messages.error(request, "An error has occurred when declining the friend request")
            except FriendshipRequest.DoesNotExist:
                messages.error(request, "Friend request not found.")
            
        else:
            messages.error(request, "Request does not exist")

    # Return an HttpResponse
    return HttpResponse
