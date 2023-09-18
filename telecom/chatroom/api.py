# Import necessary Django Rest Framework classes
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

# Import the required model and serializer
from .models import Interface
from .serializers import ChatroomModelSerializer

class ChatroomListView(generics.RetrieveAPIView, mixins.RetrieveModelMixin):
    """
    API endpoint to retrieve a list of chatrooms.
    """
    
    # Specify the source of data: all chatroom objects.
    queryset = Interface.objects.all()
    
    # Define which serializer to use for the data transformation.
    serializer_class = ChatroomModelSerializer
    
    # Custom GET method definition to retrieve the list of chatrooms.
    def get(self, request, *args, **kwargs):
        """
        Handle the GET request and return the list of chatrooms.
        """
        return self.retrieve(request, *args, **kwargs)
