from django.shortcuts import render

from rest_framework import mixins, viewsets

from . import serializers, models

class RoundViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    '''
    Get or create a new round on a course
    '''
    serializer_class = serializers.RoundSerializer

    def get_queryset(self, *args, **kwargs):
        return models.Round.objects.all()


class ScoreViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    '''
    Get or create a score for a round
    '''
    serializer_class = serializers.ScoreSerializer

    def get_queryset(self):
        return models.Score.objects.filter(round_id=self.kwargs.get('round_pk'))

    def get_object(self):
        scores = models.Score.objects.filter(round_id=self.kwargs.get('round_pk'))
        return scores.get(pk=self.kwargs.get('pk'))
