# Generated by Django 4.1.5 on 2023-01-08 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_rename_data_othercosts_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='othercosts',
            name='user',
        ),
        migrations.AddField(
            model_name='othercosts',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
