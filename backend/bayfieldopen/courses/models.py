from django.db import models


class Tee(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=256)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Hole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='holes')
    number = models.IntegerField()

    def __str__(self):
        return f'#{self.number} - {self.course.name}'


class HoleTeeStats(models.Model):
    pars = [
        (3, 'Par 3'),
        (4, 'Par 4'),
        (5, 'Par 5'),
    ]
    hole = models.ForeignKey(Hole, related_name='stats', on_delete=models.CASCADE)
    par = models.IntegerField(choices=pars)
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    yardage = models.IntegerField()

    def __str__(self):
        return f'{self.tee.name} - {self.par} - {self.yardage}'
