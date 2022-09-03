from django.db import models



# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Full Name',null=False)
    email = models.EmailField(max_length=100, verbose_name='Email', null=False)
    subject = models.CharField(max_length=200, verbose_name='Subject',null=False)
    text = models.TextField(verbose_name='Text',null=False)
    phone = models.TextField(verbose_name='Phone', default="", null=True)
    is_read = models.BooleanField(verbose_name='Read', default=False)

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Users Contacts'

    def __str__(self):
        return self.subject
