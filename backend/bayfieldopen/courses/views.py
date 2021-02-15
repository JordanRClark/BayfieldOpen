from django.shortcuts import render

from rest_framework import mixins, viewsets

from . import serializers, models

class CourseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    '''
    Returns a detailed view of a course and it's holes

    get_request:

        GET /api/v1/courses/1/

    get_response:

        {
            "id": 1,
            "par": {
                "Black": 72,
                "Blue": 72,
                "White": 72,
                "Red": 72
            },
            "yardage": {
                "Black": 6250,
                "Blue": 5729,
                "White": 5251,
                "Red": 4706
            },
            "holes": [
                {
                    "id": 1,
                    "par": {
                        "Black": 4,
                        "Blue": 4,
                        "White": 4,
                        "Red": 4
                    },
                    "yardage": {
                        "Black": 403,
                        "Blue": 357,
                        "White": 343,
                        "Red": 307
                    }
                },
                ...
                ...
            ],
            "name": "White Squirrel",
            "longitude": "-81.706706",
            "latitude": "43.402279"
        }

    get_request:

        GET /api/v1/courses/

    get_response:

        [
            {
                "id": 1,
                "par": {
                    "Black": 72,
                    "Blue": 72,
                    "White": 72,
                    "Red": 72
                },
                "yardage": {
                    "Black": 6250,
                    "Blue": 5729,
                    "White": 5251,
                    "Red": 4706
                },
                "name": "White Squirrel",
                "longitude": "-81.706706",
                "latitude": "43.402279"
            }
        ]

    '''
    serializer_class = serializers.CourseSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.CourseDetailSerializer
        elif self.action == 'list':
            return serializers.CourseSerializer

    def get_queryset(self, *args, **kwargs):
        return models.Course.objects.all()


class HoleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    '''
    Returns a detailed view of a hole

    get_request:

        GET /api/v1/courses/<ink:pk course_id>/holes/<int:pk hole_id>/

    get_response:

        {
            "id": 1,
            "par": {
                "Black": 4,
                "Blue": 4,
                "White": 4,
                "Red": 4
            },
            "yardage": {
                "Black": 403,
                "Blue": 357,
                "White": 343,
                "Red": 307
            }
        }

    get_request:

        GET /api/v1/courses/<int:pk course_id>/holes

    get_response:

        [
            {
                "id": 1,
                "par": {
                    "Black": 4,
                    "Blue": 4,
                    "White": 4,
                    "Red": 4
                },
                "yardage": {
                    "Black": 403,
                    "Blue": 357,
                    "White": 343,
                    "Red": 307
                }
            },
            ...
            {
                "id": 18,
                "par": {
                    "Black": 3,
                    "Blue": 3,
                    "White": 3,
                    "Red": 3
                },
                "yardage": {
                    "Black": 205,
                    "Blue": 150,
                    "White": 150,
                    "Red": 139
                }
            }
        ]

    '''
    serializer_class = serializers.HoleSerializer

    def get_queryset(self, *args, **kwargs):
        return models.Hole.objects.filter(course_id=self.kwargs.get('course_pk'))

    def get_object(self):
        holes = models.Hole.objects.filter(course_id=self.kwargs.get('course_pk'))
        return holes.get(pk=self.kwargs.get('pk'))
