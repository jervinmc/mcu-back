# Generated by Django 4.0 on 2023-07-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_posting_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='user_id',
            field=models.IntegerField(default=0.0, verbose_name='user_id'),
        ),
    ]