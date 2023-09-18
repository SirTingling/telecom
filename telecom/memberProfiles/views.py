# ----------------------------------------------------------------------------------------------------------------------------------- >>
from django.shortcuts import render, redirect # importing the render and redirect functions from Django
from django.contrib import messages # importing the messages module from Django
from django.contrib.auth import authenticate, login, logout # importing the authenticate, login and logout functions from Django
from django.http import HttpResponse, HttpResponseRedirect # importing the HttpResponse and HttpResponseRedirect functions from Django
from django.contrib.auth.decorators import login_required # importing the login_required decorator from Django
# ----------------------------------------------------------------------------------------------------------------------------------- >>
from .models import * # importing all models from the models.py file in the same directory as this file
from requests.models import Friend , FriendshipRequest # importing all models from the models.py file in the same directory as this file
from .forms import * # importing all forms from the forms.py file in the same directory as this file
from posts.forms import * # importing all forms from the forms.py file in the same directory as this file
from posts.models import * # importing all models from the models.py file in the same directory as this file
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# 
def has_pending_friend_request(sender, receiver):
    try:
        return FriendshipRequest.objects.get(sender=sender, receiver=receiver, pending=True)
    except FriendshipRequest.DoesNotExist:
        return False

# register a new user through form submission for the Django User model
def register_new_user(request):
    """
    Handle user registration through form submission.

    Returns:
    HttpResponse: Redirects to login on success, or displays the registration form with errors.
    """
    registered = False

    # if request method is POST, POST the data entered in the form
    if request.method == 'POST':
        user_form = RegistrationUserForm(data=request.POST)
        profile_form = RegistrationUserProfileForm(request.POST, request.FILES)

        # if user_form data is valid, save it, and set the password to user.password
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # make registered status true
            registered=True

            # return success message
            messages.success(request, 'Account registered for ' + user.username)
            return redirect('login_user')
        else:
            messages.error(request, 'Error during registration') # return error message if user_form is not valid
            messages.error(request, 'There was an error while processing your request')

    # else if the request method is GET, show the RegistrationUserForm
    else:
        user_form = RegistrationUserForm()

    # return data to be rendered
    return render(request, 'site_signup.html', {'user_form': user_form, 
                        'registered':registered})



def login_user(request):
    """
    Authenticate and login the user.

    Returns:
    HttpResponse: Redirects to home on success, or displays the login form with errors.
    """
    if request.method == 'POST':
        # send a post request with the username and password
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        # credentials are valid
        if user:
            # if the user is active then log them in
            if user.is_active:
                # use the login function from Django
                login(request, user)
                return redirect('/')

            # otherwise return error message for inactive account
            else:
                messages.error(request, 'Your account has been suspended. Please contact admin')
                return redirect('login_user')

        # otherwise return error message for invalid login details
        else:
            messages.error(request, 'Invalid login details')
            return redirect('login_user')

    # then return the login form
    else:
        return render(request, 'site_login.html')



@login_required
def display_user_profile(request):
    """
    Display the profile of the logged-in user with their posts and friend information.

    Returns:
    HttpResponse: Renders the profile page with relevant information.
    """
    context = {}
    user = request.user

    # if the user is authenticated and request method is GET
    if user.is_authenticated and request.method == 'GET':
        # get forms to display
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateUserProfileForm(instance=user.profile)
        posts = UserArticle.objects.filter(user=user)

        try:
            # get the friends of logged in user
            friend = Friend.objects.get(current_user=user)
        except Friend.DoesNotExist:
            friend_list = Friend(current_user=user)
            friend_list.save()
        
        # save friend list data of logged in user in context
        friend_list = friend.friends.all()
        context['friend_list'] = friend_list

        # filter UserProfile based on if user is in the friend_list
        # this is the get the profile image of friends
        profile = UserProfile.objects.filter(user__in=friend_list)
        context['profile'] = profile

        friend_requests = None

        try:
            # get all friend requests that are still pending
            friend_requests = FriendshipRequest.objects.filter(receiver = user, pending=True)

            images_list = []
            sender_list = []
            # find the User that matches the username from friend_requests, and append the image to images_list
            for username in friend_requests:
                sender = User.objects.get(username = username)
                profile_result = UserProfile.objects.get(user = sender)
                if profile_result.image:
                    profile_img = profile_result.image.url
                    images_list.append(profile_img)
                else:
                    images_list.append(None)

                if(has_pending_friend_request(sender = sender, receiver = user) != False):
                    sender_id = has_pending_friend_request(sender = sender, receiver = user).id
                    sender_list.append(sender_id)

            sender_info = zip(friend_requests, images_list, sender_list)
            context['sender_info'] = sender_info

        except:
            pass

        # save data in context
        context['friend_requests'] = friend_requests

        context['user'] = user
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        context['posts'] = posts
    else:
        messages.error(request, 'Please login first')
        return redirect('login_user')

    return render(request, 'site_user.html', context)



@login_required
def update_user_profile(request):
    """
    Update the user's profile through form submission.

    Returns:
    HttpResponse: Redirects to edit profile on success, or displays the form with errors.
    """
    # if the user is authenticated
    if request.user.is_authenticated:
        # if request method is POST, POST the data in the RegistrationUserForm and UpdateUserProfileForm
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
            
            # if the data in the 2 forms is valid, save them
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()

                # return success message
                messages.success(request, 'Your profile has been updated successfully')
                return redirect('update_user_profile')
            else:
                # else return success message
                messages.error(request, 'There is an error when updating your profile')
        # else if request method is GET, render the UpdateUserForm and UpdateUserProfileForm
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateUserProfileForm(instance=request.user.profile)
    else:
        messages.error(request, 'Please login first')
        return redirect('login_user')

    return render(request, 'site_edit.html', {'user_form': user_form, 'profile_form': profile_form})



@login_required
def search_for_users(request):
    """
    View function to search for users based on a query string.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Renders the search results page.
    """
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the request method is POST
        if request.method == "POST":
            # Get the search query from the POST data
            search = request.POST['q']

            # Check if there is a user search request
            if search:
                # Filter the search through the User model and retrieve the results
                result = User.objects.filter(username__contains=search)
                
                # Get the profile image of the result users, if available
                images_list = []
                for user in result:
                    profile_result = UserProfile.objects.get(user=user)
                    if profile_result.image:
                        profile_img = profile_result.image.url
                        images_list.append(profile_img)
                    else:
                        images_list.append(None)
                
                # Combine user objects and their profile images for rendering
                search_result = zip(result, images_list)
            else:
                # If there is no search query, render the search page
                return render(request, 'site_search.html')
    else:
        # If the user is not authenticated, show an error message and redirect to the login page
        messages.error(request, 'Please login first')
        return redirect('login_user')

    # Return the search result to render in the search results page
    return render(request, "site_search.html", {'search_result': search_result})




@login_required
def user_logout(request):
    """
    Log out the currently authenticated user.

    Returns:
    HttpResponse: Redirects to the home page.
    """
    # call logout function from Django and log out the user by clearing the session
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect("/")



@login_required
def approve_friend_request(request, *args, **kwargs):
    """
    Accept a friend request from another user.

    Args:
    request_id (int): The ID of the friend request to be accepted.

    Returns:
    HttpResponse: An HTTP response based on the action's success or failure.
    """
    currentUser = request.user

    if request.method == "GET" and currentUser.is_authenticated:
        # get id of request
        req_id = kwargs.get("req_id")

        # if the req_id exists
        if req_id:
            # get the req object based on the req_id
            friend_request = FriendshipRequest.objects.get(pk=req_id)
            try:
                # call accept method on the friend_request
                friend_request.accept()
                messages.success(request, "Friend request has been accepted")

            except Exception as e:
                messages.error(request, "An error has occurred when accepting friend request")
        else:
            messages.error(request, "Request does not exist")
    return HttpResponse



@login_required
def reject_friend_request(request, *args, **kwargs):
    """
    Decline a pending friend request.
    
    Args:
    - request: The HTTP request object.
    - req_id: ID of the friend request to be declined.
    
    Returns:
    - HTTP response indicating the outcome of the operation.
    """
    currentUser = request.user

    if request.method == "GET" and currentUser.is_authenticated:
        # get id of request
        req_id = kwargs.get("req_id")

        # if the req_id exists
        if req_id:
            # get the req object based on the req_id
            friend_request = FriendshipRequest.objects.get(pk=req_id)
            try:
                # call decline method on the friend_request
                friend_request.decline()
                messages.success(request, "Friend request has been declined")
            except Exception as e:
                messages.error(request, "An error has occurred when declining friend request")
        else:
            messages.error(request, "Request does not exist")
    return HttpResponse