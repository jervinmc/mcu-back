# Generated by Django 4.0.1 on 2022-12-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='posting_views',
            field=models.IntegerField(default=0.0, verbose_name='posting_views'),
        ),
    ]
