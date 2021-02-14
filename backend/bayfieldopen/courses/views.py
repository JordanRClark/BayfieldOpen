from django.shortcuts import render

from . import serializers

# Create your views here.
class CourseViewSet(mixins.ListModelView, mixins.RetrieveModelMixin):
    serializer_class = serializers.CourseSerializer
