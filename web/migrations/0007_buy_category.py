# Generated by Django 4.1.5 on 2023-01-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_customers_alter_buy_from_type_alter_orders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='category',
            field=models.ManyToManyField(to='web.category'),
        ),
    ]