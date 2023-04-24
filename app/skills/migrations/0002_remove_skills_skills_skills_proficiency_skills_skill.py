# Generated by Django 4.1.2 on 2023-04-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='skills',
        ),
        migrations.AddField(
            model_name='skills',
            name='proficiency',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='proficiency'),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='skill'),
        ),
    ]
