from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('(?P<course_pk>\d+)/holes', views.HoleViewSet, basename='holes')
router.register('', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('courses/', include(router.urls))
]
