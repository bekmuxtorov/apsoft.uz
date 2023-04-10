from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='clients')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Full name')
    email = models.EmailField(max_length=200, verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Subject')
    message = models.TextField(max_length=400, verbose_name='Message')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
