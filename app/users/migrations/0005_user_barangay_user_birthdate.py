# Generated by Django 4.0.1 on 2022-07-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='barangay',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='barangay'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='birthdate'),
        ),
    ]
