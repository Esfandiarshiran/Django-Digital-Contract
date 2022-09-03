import os

from django.db import models

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"team_members/{final_name}"


class TeamMembers(models.Model):
    title = models.CharField(max_length=150, verbose_name="Name")
    job_title = models.CharField(max_length=150, verbose_name="Job Title")
    introduce = models.CharField(max_length=300, verbose_name="Introduce")
    picture = models.ImageField(upload_to=upload_image_path, null=False, blank=False, verbose_name='Picture')
    email = models.CharField(max_length=150, verbose_name="Email")
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.title