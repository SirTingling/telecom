import os
from django.conf import settings
from django.contrib import messages
# importing the OS module and other components from Django
import os # Import the OS module
from django.conf import settings  # Import the settings module from Django
from django.contrib import messages # Import the messages module from Django
from django.shortcuts import render # Import the render module from Django
from django.core.files.storage import FileSystemStorage # Import the FileSystemStorage module from Django
from django.http import HttpResponseRedirect # Import the HttpResponseRedirect module from Django
# importing the User model and other components from Django's built-in authentication system.
# ---------------------------------------------------------------------------------------------------------------------- >>
from .models import * # Import all models from the posts app
from .forms import *    # Import all forms from the posts app
from memberProfiles.models import * # Import all models from the memberProfiles app
from memberProfiles.forms import * # Import all forms from the memberProfiles app
from requests.models import * # Import all models from the requests app
# ---------------------------------------------------------------------------------------------------------------------- >>
# The home of the application for displaying posts and creating posts
def home(request, *args, **kwargs):
    """
    Display and handle the creation of posts.

    - For authenticated users, their posts and their friends' posts are displayed.
    - Allows authenticated users to create new posts.
    - Provides profile update form for the authenticated users.
    """
    context = {}
    currentUser = request.user

    # if the request method is POST and the user is authenticated
    if request.method == "POST" and currentUser.is_authenticated:
        # the post_form is the UserPostForm with the request.POST and request.FILES
        post_form = UserPostForm(request.POST, request.FILES)
        # the profile_form is the UpdateUserProfileForm with the request.POST and request.FILES
        # checking if the request.FILES is empty because the profile image is optional
        if post_form.is_valid():
            # get the cleaned_data
            content = post_form.cleaned_data.get("content")
            try: 
                # request for file upload where the input name is 'postImage'
                request_file = request.FILES['postImage']
                # location of media folder 
                url = os.path.join(settings.MEDIA_ROOT)
                fss = FileSystemStorage(location=url)
                # stores image at media/postImage directory
                file = fss.save(f"postImage/{str(request_file)}", request_file)

                # create a UserArticle object with the content, file, currentUser information
                new_post = UserArticle.objects.create(content=content, content_image=file, user=currentUser)

                # return success message
                messages.success(request, 'Successfully uploaded a new post with image')
                return HttpResponseRedirect("/")
            except:
                # if there is no image uploaded by the user, create the UserArticle with only the content and currenUser
                new_post = UserArticle.objects.create(content=content, user=currentUser)

                # return success message
                messages.success(request, 'Successfully uploaded a new post and correct image')
                return HttpResponseRedirect("/")

    # if the user is authenticated
    if currentUser.is_authenticated:
        # collect the profile information of the currentUser
        profile_form = UpdateUserProfileForm(instance=currentUser.profile)
        context['profile_form'] = profile_form

        """
        Handle the creation of new posts by authenticated users.

        Parameters:
        - request (HttpRequest): The request instance

        Returns:
        - dict: A dictionary with the message after handling post creation.
        """

        friend_list = []
        try:
            # get the friends of the currentUser
            currentUser_friend_list = Friend.objects.get(current_user=currentUser)
            # append each friend object to the friend_list
            for friend in currentUser_friend_list.friends.all():
                friend_list.append(friend)
        except Friend.DoesNotExist:
            pass

        # if there are friend in the friend_list, display currentUser's post and their friends' posts
        if friend_list != []:
            # include currentUser to list before filtering
            friend_list.append(currentUser)

            # filter UserPost based on if user is in the friend_list
            # order by timestamp and reverse filtered result so that posts are correctly displayed on the home page
            # (new post displayed before old post)
            posts = reversed(UserArticle.objects.filter(user__in=friend_list).order_by('timestamp'))
            context['posts'] = posts

            # filter UserProfile based on if user is in the friend_list
            # this is to get the profile image of friends
            profile = UserProfile.objects.filter(user__in=friend_list)
            context['profile'] = profile
            
        # else if friend_list is empty
        else:
            # display own posts only
            # order by timestamp and reverse filtered result so that posts are correctly displayed on the home page
            # (new post displayed before old post)
            posts = reversed(UserArticle.objects.filter(user=currentUser).order_by('timestamp'))
            context['posts'] = posts

            # filter UserProfile based on if user is in the friend_list
            # this is to get the profile image of friends
            profile = UserProfile.objects.get(user=currentUser)
            context['profile'] = profile

        # for the navbar in site_header.html to display the active state of the home icon correctly
        context['navbar'] = "home"
    return render(request, "post.html", context)