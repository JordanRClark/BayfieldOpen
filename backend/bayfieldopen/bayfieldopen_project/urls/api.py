from django.contrib import admin
from django.urls import path, include

apipatterns = [
    path('', include('courses.urls')),
    path('', include('scores.urls')),
]

urlpatterns = [path('api/v1/', include((apipatterns, 'api'), namespace='v1'))]
