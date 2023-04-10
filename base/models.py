from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=_('clients'))
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200, verbose_name=_('Full name'))
    email = models.EmailField(max_length=200, verbose_name=_('Email'))
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    message = models.TextField(max_length=400, verbose_name=_('Message'))
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
