# Generated by Django 4.0.5 on 2022-08-23 21:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('person', '0003_remove_person_id_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rule',
            new_name='Warrant',
        ),
    ]
