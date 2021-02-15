from django.conf import settings
from django.db import models

class Round(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    tee = models.ForeignKey('courses.Tee', on_delete=models.CASCADE)

    def overall_score(self):
        score = 0
        par = 0
        for hole_score in self.holes.all():
            score += hole_score.score
            par += hole_score.hole.stats.get(tee=self.tee).par
        return score - par

    def __str__(self):
        return f'{self.user.email} - {self.course.name} - {self.tee.name}'


class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='holes')
    hole = models.ForeignKey('courses.Hole', on_delete=models.CASCADE)
    score = models.IntegerField()
