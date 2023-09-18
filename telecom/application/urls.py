"""Telecom URL Configuration

This module maps URLs to their associated views in the Telecom application.
"""

# Standard library imports
from django.contrib import admin # Importing the admin module from Django
from django.urls import path, include # Importing the path and include functions from Django
# ------------------------------------------------------------------------------------------------------------------------------------------------- >>
from django.conf import settings # Importing the settings module from Django
from django.conf.urls.static import static # Importing the static module from Django
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Importing the staticfiles module from Django
from rest_framework.schemas import get_schema_view # Importing the get_schema_view function from Django REST Framework
from django.views.generic import TemplateView # Importing the TemplateView class from Django
# ------------------------------------------------------------------------------------------------------------------------------------------------- >>
urlpatterns = [
    path('', include('posts.urls')),
    path('', include('chatroom.urls')),
    path('', include('memberProfiles.urls')),
    path('', include('requests.urls')),
    # -------------------------------------------------------------------------------------------------------------------------------------------------
    # Admin portal
    path('admin/', admin.site.urls, name='admin_portal'),
    # -------------------------------------------------------------------------------------------------------------------------------------------------
    # API schema: Provides structured information about the REST API
    path('apischema/', get_schema_view(
        title="Telecom Project REST API",
        description="RESTful API documentation for the Telecom application.", 
        version="1.0.0"
    ), name='openapi-schema'),
    # restapi was used here to avoid conflict with the rest_framework module
    # -------------------------------------------------------------------------------------------------------------------------------------------------
    path('swaggerui/', TemplateView.as_view(
        template_name='site_swagger.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
# ------------------------------------------------------------------------------------------------------------------------------------------------- >>

# Handle media and static files
# In development mode, Django serves media files directly. 
# In production, the server configuration should manage this.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
# ------------------------------------------------------------------------------------------------------------------------------------------------- >>