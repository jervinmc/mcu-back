# Generated by Django 4.0.1 on 2022-12-25 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcement_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='views',
        ),
    ]