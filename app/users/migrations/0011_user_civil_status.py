# Generated by Django 4.1.2 on 2023-04-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='civil_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='civil_status'),
        ),
    ]
