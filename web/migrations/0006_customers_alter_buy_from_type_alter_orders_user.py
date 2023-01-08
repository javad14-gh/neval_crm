# Generated by Django 4.1.5 on 2023-01-08 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_buy_from_category_remove_othercosts_user_orders_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='buy_from',
            name='type',
            field=models.CharField(choices=[('store', 'store'), ('site', 'site')], max_length=255),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customers'),
        ),
    ]
