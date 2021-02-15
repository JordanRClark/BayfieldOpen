from django.core.management.base import BaseCommand

from courses.models import Course, Hole, Tee, HoleTeeStats


class Command(BaseCommand):
    help = 'Sets up demo courses'

    def handle(self, *args, **kwargs):
        # White squirrel
        course = Course.objects.create(name='White Squirrel', latitude=43.402279, longitude=-81.706706)

        black, _ = Tee.objects.get_or_create(name='Black')
        blue, _ = Tee.objects.get_or_create(name='Blue')
        white, _ = Tee.objects.get_or_create(name='White')
        red, _ = Tee.objects.get_or_create(name='Red')

        hole1, _ = Hole.objects.get_or_create(course=course, number=1)
        HoleTeeStats.objects.get_or_create(hole=hole1, par=4, tee=black, yardage=403)
        HoleTeeStats.objects.get_or_create(hole=hole1, par=4, tee=blue, yardage=357)
        HoleTeeStats.objects.get_or_create(hole=hole1, par=4, tee=white, yardage=343)
        HoleTeeStats.objects.get_or_create(hole=hole1, par=4, tee=red, yardage=307)

        hole2, _ = Hole.objects.get_or_create(course=course, number=2)
        HoleTeeStats.objects.get_or_create(hole=hole2, par=3, tee=black, yardage=227)
        HoleTeeStats.objects.get_or_create(hole=hole2, par=3, tee=blue, yardage=218)
        HoleTeeStats.objects.get_or_create(hole=hole2, par=3, tee=white, yardage=179)
        HoleTeeStats.objects.get_or_create(hole=hole2, par=3, tee=red, yardage=150)

        hole3, _ = Hole.objects.get_or_create(course=course, number=3)
        HoleTeeStats.objects.get_or_create(hole=hole3, par=4, tee=black, yardage=311)
        HoleTeeStats.objects.get_or_create(hole=hole3, par=4, tee=blue, yardage=301)
        HoleTeeStats.objects.get_or_create(hole=hole3, par=4, tee=white, yardage=289)
        HoleTeeStats.objects.get_or_create(hole=hole3, par=4, tee=red, yardage=277)

        hole4, _ = Hole.objects.get_or_create(course=course, number=4)
        HoleTeeStats.objects.get_or_create(hole=hole4, par=4, tee=black, yardage=348)
        HoleTeeStats.objects.get_or_create(hole=hole4, par=4, tee=blue, yardage=318)
        HoleTeeStats.objects.get_or_create(hole=hole4, par=4, tee=white, yardage=297)
        HoleTeeStats.objects.get_or_create(hole=hole4, par=4, tee=red, yardage=286)

        hole5, _ = Hole.objects.get_or_create(course=course, number=5)
        HoleTeeStats.objects.get_or_create(hole=hole5, par=5, tee=black, yardage=475)
        HoleTeeStats.objects.get_or_create(hole=hole5, par=5, tee=blue, yardage=432)
        HoleTeeStats.objects.get_or_create(hole=hole5, par=5, tee=white, yardage=423)
        HoleTeeStats.objects.get_or_create(hole=hole5, par=5, tee=red, yardage=421)

        hole6, _ = Hole.objects.get_or_create(course=course, number=6)
        HoleTeeStats.objects.get_or_create(hole=hole6, par=4, tee=black, yardage=279)
        HoleTeeStats.objects.get_or_create(hole=hole6, par=4, tee=blue, yardage=270)
        HoleTeeStats.objects.get_or_create(hole=hole6, par=4, tee=white, yardage=262)
        HoleTeeStats.objects.get_or_create(hole=hole6, par=4, tee=red, yardage=251)

        hole7, _ = Hole.objects.get_or_create(course=course, number=7)
        HoleTeeStats.objects.get_or_create(hole=hole7, par=4, tee=black, yardage=355)
        HoleTeeStats.objects.get_or_create(hole=hole7, par=4, tee=blue, yardage=349)
        HoleTeeStats.objects.get_or_create(hole=hole7, par=4, tee=white, yardage=315)
        HoleTeeStats.objects.get_or_create(hole=hole7, par=4, tee=red, yardage=265)

        hole8, _ = Hole.objects.get_or_create(course=course, number=8)
        HoleTeeStats.objects.get_or_create(hole=hole8, par=5, tee=black, yardage=432)
        HoleTeeStats.objects.get_or_create(hole=hole8, par=5, tee=blue, yardage=390)
        HoleTeeStats.objects.get_or_create(hole=hole8, par=5, tee=white, yardage=344)
        HoleTeeStats.objects.get_or_create(hole=hole8, par=5, tee=red, yardage=308)

        hole9, _ = Hole.objects.get_or_create(course=course, number=9)
        HoleTeeStats.objects.get_or_create(hole=hole9, par=3, tee=black, yardage=205)
        HoleTeeStats.objects.get_or_create(hole=hole9, par=3, tee=blue, yardage=174)
        HoleTeeStats.objects.get_or_create(hole=hole9, par=3, tee=white, yardage=155)
        HoleTeeStats.objects.get_or_create(hole=hole9, par=3, tee=red, yardage=155)

        hole10, _ = Hole.objects.get_or_create(course=course, number=10)
        HoleTeeStats.objects.get_or_create(hole=hole10, par=4, tee=black, yardage=425)
        HoleTeeStats.objects.get_or_create(hole=hole10, par=4, tee=blue, yardage=382)
        HoleTeeStats.objects.get_or_create(hole=hole10, par=4, tee=white, yardage=326)
        HoleTeeStats.objects.get_or_create(hole=hole10, par=4, tee=red, yardage=292)

        hole11, _ = Hole.objects.get_or_create(course=course, number=11)
        HoleTeeStats.objects.get_or_create(hole=hole11, par=4, tee=black, yardage=354)
        HoleTeeStats.objects.get_or_create(hole=hole11, par=4, tee=blue, yardage=342)
        HoleTeeStats.objects.get_or_create(hole=hole11, par=4, tee=white, yardage=276)
        HoleTeeStats.objects.get_or_create(hole=hole11, par=4, tee=red, yardage=269)

        hole12, _ = Hole.objects.get_or_create(course=course, number=12)
        HoleTeeStats.objects.get_or_create(hole=hole12, par=3, tee=black, yardage=182)
        HoleTeeStats.objects.get_or_create(hole=hole12, par=3, tee=blue, yardage=174)
        HoleTeeStats.objects.get_or_create(hole=hole12, par=3, tee=white, yardage=158)
        HoleTeeStats.objects.get_or_create(hole=hole12, par=3, tee=red, yardage=158)

        hole13, _ = Hole.objects.get_or_create(course=course, number=13)
        HoleTeeStats.objects.get_or_create(hole=hole13, par=5, tee=black, yardage=434)
        HoleTeeStats.objects.get_or_create(hole=hole13, par=5, tee=blue, yardage=423)
        HoleTeeStats.objects.get_or_create(hole=hole13, par=5, tee=white, yardage=409)
        HoleTeeStats.objects.get_or_create(hole=hole13, par=5, tee=red, yardage=322)

        hole14, _ = Hole.objects.get_or_create(course=course, number=14)
        HoleTeeStats.objects.get_or_create(hole=hole14, par=4, tee=black, yardage=439)
        HoleTeeStats.objects.get_or_create(hole=hole14, par=4, tee=blue, yardage=402)
        HoleTeeStats.objects.get_or_create(hole=hole14, par=4, tee=white, yardage=314)
        HoleTeeStats.objects.get_or_create(hole=hole14, par=4, tee=red, yardage=282)

        hole15, _ = Hole.objects.get_or_create(course=course, number=15)
        HoleTeeStats.objects.get_or_create(hole=hole15, par=4, tee=black, yardage=289)
        HoleTeeStats.objects.get_or_create(hole=hole15, par=4, tee=blue, yardage=276)
        HoleTeeStats.objects.get_or_create(hole=hole15, par=4, tee=white, yardage=262)
        HoleTeeStats.objects.get_or_create(hole=hole15, par=4, tee=red, yardage=191)

        hole16, _ = Hole.objects.get_or_create(course=course, number=16)
        HoleTeeStats.objects.get_or_create(hole=hole16, par=4, tee=black, yardage=349)
        HoleTeeStats.objects.get_or_create(hole=hole16, par=4, tee=blue, yardage=286)
        HoleTeeStats.objects.get_or_create(hole=hole16, par=4, tee=white, yardage=278)
        HoleTeeStats.objects.get_or_create(hole=hole16, par=4, tee=red, yardage=239)

        hole17, _ = Hole.objects.get_or_create(course=course, number=17)
        HoleTeeStats.objects.get_or_create(hole=hole17, par=5, tee=black, yardage=538)
        HoleTeeStats.objects.get_or_create(hole=hole17, par=5, tee=blue, yardage=485)
        HoleTeeStats.objects.get_or_create(hole=hole17, par=5, tee=white, yardage=471)
        HoleTeeStats.objects.get_or_create(hole=hole17, par=5, tee=red, yardage=394)

        hole18, _ = Hole.objects.get_or_create(course=course, number=18)
        HoleTeeStats.objects.get_or_create(hole=hole18, par=3, tee=black, yardage=205)
        HoleTeeStats.objects.get_or_create(hole=hole18, par=3, tee=blue, yardage=150)
        HoleTeeStats.objects.get_or_create(hole=hole18, par=3, tee=white, yardage=150)
        HoleTeeStats.objects.get_or_create(hole=hole18, par=3, tee=red, yardage=139)
