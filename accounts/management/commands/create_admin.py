import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crea superusuario desde variables de entorno ADMIN_USER, ADMIN_EMAIL, ADMIN_PASSWORD'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('ADMIN_USER', 'admin')
        email = os.environ.get('ADMIN_EMAIL', '')
        password = os.environ.get('ADMIN_PASSWORD', '')

        if not password:
            self.stdout.write(self.style.WARNING('ADMIN_PASSWORD no definido, se omite.'))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Usuario "{username}" ya existe.')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado.'))
