# Generated by Django 4.1 on 2022-09-01 08:22

import Docusign_AboutUs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Name')),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('introduce', models.CharField(max_length=300, verbose_name='Introduce')),
                ('picture', models.ImageField(upload_to=Docusign_AboutUs.models.upload_image_path, verbose_name='Picture')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
