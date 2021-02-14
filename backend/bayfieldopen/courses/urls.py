from django.urls import include
from rest_framework.routers import SimpleRouter

from .views import CourseView

router = SimpleRouter()

router.register('', CourseView, baasename='courses')

urlpatterns = [
    path('courses/', include(router.urls))
]
