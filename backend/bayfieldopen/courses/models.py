from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=256)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Hole(models.Model):
    pars = [
        ('Par 3', 3),
        ('Par 4', 4),
        ('Par 5', 5),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    par = models.CharField(max_length=5, choices=pars)
    number = models.IntegerField()

    def __str__(self):
        return f'#{self.number} - {self.par} - {self.course.name}'
