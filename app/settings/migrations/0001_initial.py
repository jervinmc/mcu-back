# Generated by Django 4.0.1 on 2022-12-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=255, null=True, verbose_name='semester')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
