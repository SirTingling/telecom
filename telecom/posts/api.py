# importing from the Django REST framework components
from .models import UserArticle # Explicitly import the required model from the posts app
from .forms import UserPostForm # Explicitly import the required form from the posts app
from .serializers import UserPostDetailSerializer # Explicitly import the required serializer from the posts app
# ------------------------------------------------------------------------------------------------------------------------------------------------------- >>
from rest_framework import generics, mixins

# UserPostRetrieveView:
# API endpoint to retrieve a single UserPost instance based on its primary key.
# Endpoint: api/userpost/<int:pk>/
class UserPostRetrieveView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    # Specifies the set of all UserPost objects as the dataset from which to retrieve
    queryset = UserArticle.objects.all()
    
    # Specifies the serializer to convert UserPost instances to JSON representation
    serializer_class = UserPostDetailSerializer
    
    # Handle GET request and return a single UserPost instance
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# UserPostCreateView:
# API endpoint to create a new UserPost instance.
# Endpoint: api/createpost/
class UserPostCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    # Specifies the set of all UserPost objects as the base dataset
    # Note: For creation, the actual set of objects isn't usually relevant, but DRF expects queryset
    queryset = UserArticle.objects.all()
    
    # Specifies the serializer to convert incoming JSON to a UserPost instance
    serializer_class = UserPostDetailSerializer
    
    # Form class is specified for potential use in Django's Browsable API
    form_class = UserPostForm

    # Handle POST request and create a new UserPost instance
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
