# importing the django apps AppConfig class from Django
from django.urls import re_path # importing the re_path function from Django
from . import users # importing the users module from the chatroom app

# Websocket routes are defined below. The use of 'ws/' as a prefix clearly
# demarcates them from typical HTTP routes, similar to how 'api/' is commonly
# used for REST API endpoints.
websocket_routes = [
    # This route captures websocket connections aimed at individual chatrooms.
    # The chatroom name is dynamically extracted from the URL and passed 
    # to the ChatroomWebSocketUser for further handling.
    re_path(r'ws/chat/(?P<chatroom>\w+)/$', users.ChatroomWebSocketUser.as_asgi()),
]
# ----------------------------------------------------------------------------------------------------------------------------------- >> 
