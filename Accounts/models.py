from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Accounts Model starts Here


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(unique=True, max_length=50)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    profile_pic = models.ImageField(upload_to='Accounts/Profile', blank=True)

    def __str__(self):
        return self.user.username

