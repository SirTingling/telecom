# importing the django apps AppConfig class from Django
from django.contrib import messages # importing the messages module from Django
from django.shortcuts import render, redirect # importing the render and redirect functions from Django
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# importing the ChatRoomCreationForm from the chatroom app
from .forms import ChatRoomCreationForm
from .models import *
# importing the UserProfile model from the memberProfiles app
# ----------------------------------------------------------------------------------------------------------------------------------- >>
from memberProfiles.models import *
from memberProfiles.forms import UpdateUserProfileForm
# ----------------------------------------------------------------------------------------------------------------------------------- >>

def chat(request):
    """
    Render the chat dashboard. Allow users to see and create new chatrooms.
    
    This view handles both the display of the chat dashboard and the creation 
    of new chatrooms when the user submits the creation form.
    """
    context = {}
    if request.user.is_authenticated:
        if request.method == "POST":
            chatroomForm = ChatRoomCreationForm(request.POST)
            if chatroomForm.is_valid():
                chatroomForm.save()
                chatroom = request.POST['chatroom']
                messages.success(request, f'Chatroom "{chatroom}" has been created successfully!')
                return redirect('/chat/' + chatroom)
            else:
                messages.error(request, 'Error encountered! Unable to create the chatroom. Please ensure details are correct.')
                return redirect('chat')
        else:
            # Preparing data for chat dashboard display
            profile_form = UpdateUserProfileForm(instance=request.user.profile)
            chatroom = Interface.objects.all()

            # show create chatroom form
            chatroomForm = ChatRoomCreationForm()

            # save data to chatroom
            context['profile_form'] = profile_form
            context['navbar'] = "chat"
            context['chatroom'] = chatroom
            context['chatroomForm'] = chatroomForm
        return render(request, 'chat_dashboard.html', context)
    else:
        messages.error(request, 'Please login first')
        return redirect('login_user')



def view_chatroom(request, chatroom_name):
    """
    Render a specific chatroom, allowing users to view and send messages.
    
    This view displays a specific chatroom's content and allows logged-in users 
    to participate in the chat.
    """
    context = {}
    if request.user.is_authenticated:
        if request.method == "GET":
            profile_form = UpdateUserProfileForm(instance=request.user.profile)
            context['profile_form'] = profile_form
            context['navbar'] = "chat"
            context['chatroom_name'] = chatroom_name

        return render(request, 'chatroom.html', context)
    else:
        messages.error(request, 'You must be logged in to view the chatroom.')
        return redirect('login_user')


# ----------------------------------------------------------------------------------------------------------------------------------- >>
def remove_chatroom(request, chatroom_name):
    """
    Handle the deletion of a chatroom.
    
    This view deletes a specific chatroom and provides feedback to the user 
    on the outcome of the action.
    """
    # Delete the chatroom and redirect to the chat dashboard
    try:
        chatroom = Interface.objects.get(chatroom = chatroom_name)
        chatroom.delete()
        # successfully charoom successfully deleted
        messages.success(request, f'Chatroom "{chatroom_name}" has been removed successfully!')
        return redirect('chat') # redirect to the chat dashboard
    except:
        messages.error(request, 'The request was unsuccessful, chatroom not deleted.') # error when deleting the chatroom
        return redirect('chat') # redirect to the chat dashboard    
# ----------------------------------------------------------------------------------------------------------------------------------- >>
