from rest_framework import serializers

from courses.serializers import CourseSerializer

from . import models

class ScoreSerializer(serializers.ModelSerializer):
    par = serializers.SerializerMethodField()
    class Meta:
        model = models.Score
        fields = [
            'id',
            'hole',
            'score',
            'par',
        ]

    def get_par(self, instance):
        return instance.hole.stats.get(tee=instance.round.tee).par

class RoundSerializer(serializers.ModelSerializer):
    holes = ScoreSerializer(many=True)
    overall_score = serializers.SerializerMethodField()
    course = CourseSerializer()
    class Meta:
        model = models.Round
        fields = [
            'id',
            'holes',
            'overall_score',
            'user',
            'course',
        ]

    def get_overall_score(self, instance):
        return instance.overall_score()
