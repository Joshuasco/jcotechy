from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings as _S

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='joshua1').exists():
            User.objects.create_superuser(
                username=_S.ADMIN_USER,
                password=_S.ADMIN_PASSWD  )
        print('##################################')        
        print('Superuser has been created.')
        print('##################################') 