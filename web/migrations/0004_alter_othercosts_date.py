# Generated by Django 4.1.5 on 2023-01-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_othercosts_user_othercosts_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othercosts',
            name='date',
            field=models.DateField(),
        ),
    ]