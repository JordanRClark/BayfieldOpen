from rest_framework import serializers

from . import models

class HoleSerializer(serializers.ModelSerializer):
    par = serializers.SerializerMethodField()
    yardage = serializers.SerializerMethodField()
    class Meta:
        model = models.Hole
        fields = [
            'id',
            'par',
            'yardage',
        ]

    def get_par(self, instance):
        hole_pars = {}
        for stats in instance.stats.all():
            hole_pars[stats.tee.name] = stats.par
        return hole_pars

    def get_yardage(self, instance):
        hole_yardage = {}
        for stats in instance.stats.all():
            hole_yardage[stats.tee.name] = stats.yardage
        return hole_yardage


class CourseSerializer(serializers.ModelSerializer):
    par = serializers.SerializerMethodField()
    yardage = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = '__all__'

    def get_par(self, instance):
        course_pars = {}
        for hole in instance.holes.all():
            for stats in hole.stats.all():
                if stats.tee.name not in course_pars.keys():
                    course_pars[stats.tee.name] = 0
                course_pars[stats.tee.name] += stats.par
        return course_pars

    def get_yardage(self, instance):
        course_stats = {}
        for hole in instance.holes.all():
            for stats in hole.stats.all():
                if stats.tee.name not in course_stats.keys():
                    course_stats[stats.tee.name] = 0
                course_stats[stats.tee.name] += stats.yardage
        return course_stats

class CourseDetailSerializer(CourseSerializer):
    holes = HoleSerializer(many=True)
    class Meta:
        model = models.Course
        fields = '__all__'
