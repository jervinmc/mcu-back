# Generated by Django 4.0.1 on 2022-11-30 10:53

from django.db import migrations, models
import django.utils.timezone
import job_posting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='content')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')),
                ('image', models.ImageField(default='uploads/users_placeholder.png', upload_to=job_posting.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
