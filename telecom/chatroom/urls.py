from django.urls import include, path
from . import views
from . import api

# Description: URL patterns for the Telecom's chatroom app
from django.urls import path # Importing the path function from Django
from . import views # Importing the views module from the chatroom app
from . import api # Importing the API module from the chatroom app
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# Chat-related URL patterns
urlpatterns = [
    # Endpoint for the main chat dashboard or listing
    path('chat/', views.chat, name='chatroom'),
    
    # Endpoint to view a specific chatroom
    path('chat/<str:chatroom_name>', views.view_chatroom, name='chatroom_view'),
    
    # Endpoint to delete a specific chatroom
    path('chat/deleteChatroom/<str:chatroom_name>', views.remove_chatroom, name='remove_chatroom'),
]
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
# API-related URL patterns
urlpatterns += [
    # API endpoint to retrieve chatroom details by primary key
    path('api/chatroom/<int:pk>/', api.ChatroomListView.as_view(), name='chatroom_detail_api'),
]
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
