from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'handicap',
        ]
