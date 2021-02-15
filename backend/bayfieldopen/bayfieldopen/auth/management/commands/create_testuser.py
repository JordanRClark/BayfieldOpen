from django.core.management.base import BaseCommand

from bayfieldopen.auth.models import User

class Command(BaseCommand):
    help = 'Setup test user'

    def handle(self, *args, **kwargs):
        User.objects.create_testuser()
