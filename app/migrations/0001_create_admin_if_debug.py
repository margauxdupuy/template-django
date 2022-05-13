from django.db import migrations
from django.conf import settings
from django.utils import timezone


def create_admin_if_debug(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    superuser = User.objects.create_superuser(
        username='admin',
        email='admin@admin.adm',
        password='admin',
        last_login=timezone.now())

    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_admin_if_debug)
    ] if settings.DEBUG is True else []

