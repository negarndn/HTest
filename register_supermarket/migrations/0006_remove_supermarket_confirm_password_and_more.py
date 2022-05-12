# Generated by Django 4.0.4 on 2022-05-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_supermarket', '0005_supermarket_confirm_password_supermarket_sms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermarket',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='city',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='id_sup',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='name_sup',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]