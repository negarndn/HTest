# Generated by Django 4.0.4 on 2022-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
