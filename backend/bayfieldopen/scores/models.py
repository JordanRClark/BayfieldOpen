from django.conf import settings
from django.db import models

class Round(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    tee = models.ForeignKey('courses.Tee', on_delete=models.CASCADE)

    def par_score(self):
        score = 0
        par = 0
        for hole_score in self.holes.all():
            score += hole_score.score
            par += hole_score.hole.stats.get(tee=self.tee).par
        return score - par

    def overall_score(self):
        return sum([hole_score.score for hole_score in self.holes.all()])

    def fir_percentage(self):
        num_holes = self.holes.all().count()
        num_firs = 0
        for hole_score in self.holes.all():
            if hole_score.fir:
                num_firs += 1
        if num_firs == 0:
            return 0
        return round((num_firs / num_holes) * 100, 2)

    def gir_percentage(self):
        num_holes = self.holes.all().count()
        num_girs = 0
        for hole_score in self.holes.all():
            if hole_score.gir:
                num_girs += 1
        if num_girs == 0:
            return 0
        return round((num_girs / num_holes) * 100, 2)


    def __str__(self):
        return f'{self.user.email} - {self.course.name} - {self.tee.name}'


class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='holes')
    hole = models.ForeignKey('courses.Hole', on_delete=models.CASCADE)
    score = models.IntegerField()
    fir = models.BooleanField(default=False)
    gir = models.BooleanField(default=False)
    putts = models.IntegerField()
