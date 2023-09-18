# models.py imports
from .models import Friend, FriendshipRequest

# serializers.py imports
from .serializers import UserWithFriendsSerializer, FriendshipInteractionSerializer

# rest_framework imports
from rest_framework import generics, mixins

class FriendDetailView(generics.ListAPIView, mixins.RetrieveModelMixin):
    """
    API view to retrieve details for a specific friend using its primary key.
    Endpoint: api/friendlist/<int:pk>/
    """

    # Specifies the dataset to be used for this view
    queryset = Friend.objects.all()

    # Specifies the serializer to transform the data
    serializer_class = UserWithFriendsSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for this view.
        Args:
        - request: The incoming request object.
        - *args: Additional arguments.
        - **kwargs: Additional keyword arguments (includes pk for the friend).

        Returns:
        A response object containing serialized details of a specific friend.
        """
        return self.retrieve(request, *args, **kwargs)


class FriendRequestDetailView(generics.ListAPIView, mixins.RetrieveModelMixin):
    """
    API view to retrieve details for a specific friend request using its primary key.
    Endpoint: api/friendrequest/<int:pk>/
    """

    # Specifies the dataset to be used for this view
    queryset = FriendshipRequest.objects.all()

    # Specifies the serializer to transform the data
    serializer_class = FriendshipInteractionSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for this view.
        Args:
        - request: The incoming request object.
        - *args: Additional arguments.
        - **kwargs: Additional keyword arguments (includes pk for the friend request).

        Returns:
        A response object containing serialized details of a specific friend request.
        """
        return self.retrieve(request, *args, **kwargs)
