# import the necessary modules for telecom'd requests app
from django.urls import path # Importing the path function from Django
from . import views # Importing the views module from the requests app
from . import api # Importing the API module from the requests app
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
urlpatterns = [
    # Friend-related views
    path('friendDetail/<str:username>', views.friendDetail, name='friendDetail'),
    path('request/', views.initiate_friend_request, name='initiate_friend_request'), ####### ### names matching with the tests and the apis and the views
    path('cancel', views.handle_friend_request, name='handle_friend_request'), #######
    path('unfriend/', views.unfriend, name='unfriend'),
    
    # Handling friend requests with specific ID
    path('approve_friend_request/<req_id>/', views.approve_friend_request, name='approve_friend_request'),
    path('reject_friend_request/<req_id>/', views.reject_friend_request, name='reject_friend_request'), ####### ### names matching with the tests and the apis and the views

    # API Endpoints
    path('api/friendlist/<int:pk>/', api.FriendDetailView.as_view(), name='FriendDetailView'),  ### names matching with the tests and the apis and the views
    path('api/friendrequest/<int:pk>/', api.FriendRequestDetailView.as_view(), name='FriendRequestDetailView'), ######
]
# -------------------------------------------------------------------------------------------------------------------------------------------------- >>
