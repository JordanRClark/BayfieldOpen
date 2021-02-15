from django.conf import settings
from django.urls import include, path

from .admin import urlpatterns as admin_patterns
from .api import urlpatterns as api_patterns

urlpatterns = (
    admin_patterns
    + api_patterns
)
