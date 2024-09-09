from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    nickname = models.CharField(max_length=50)
    birth = models.DateField()
    gender = models.CharField(choices=gender_choices, max_length=1, null=True, blank=True)
    introduction = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.username
    
    def soft_delete(self):
        self.is_active = False
        self.save()
        return True