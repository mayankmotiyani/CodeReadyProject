from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ('I prefer not to say','I prefer not to say'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    #avatar
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.user}'