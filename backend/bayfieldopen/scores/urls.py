from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('(?P<round_pk>\d+)/scores', views.ScoreViewSet, basename='scores')
router.register('', views.RoundViewSet, basename='rounds')

urlpatterns = [
    path('rounds/', include(router.urls))
]
