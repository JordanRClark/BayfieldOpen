from rest_framework import serializers

from courses.serializers import CourseSerializer
from bayfieldopen.auth.serializers import UserSerializer

from . import models

class ScoreSerializer(serializers.ModelSerializer):
    par = serializers.SerializerMethodField()
    class Meta:
        model = models.Score
        fields = [
            'id',
            'hole',
            'score',
            'fir',
            'gir',
            'putts',
            'par',
        ]

    def get_par(self, instance):
        return instance.hole.stats.get(tee=instance.round.tee).par

class RoundSerializer(serializers.ModelSerializer):
    holes = ScoreSerializer(many=True)
    par_score = serializers.SerializerMethodField()
    overall_score = serializers.SerializerMethodField()
    course = CourseSerializer()
    user = UserSerializer()
    fir_percentage = serializers.SerializerMethodField()
    gir_percentage = serializers.SerializerMethodField()
    class Meta:
        model = models.Round
        fields = [
            'id',
            'holes',
            'overall_score',
            'par_score',
            'fir_percentage',
            'gir_percentage',
            'user',
            'course',
        ]

    def get_par_score(self, instance):
        return instance.par_score()

    def get_overall_score(self, instance):
        return instance.overall_score()

    def get_fir_percentage(self, instance):
        return instance.fir_percentage()

    def get_gir_percentage(self, instance):
        return instance.gir_percentage()



