from django.db import models
from django.contrib.auth.models import User

# Accounts Model starts Here


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(unique=True, max_length=50)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(upload_to='Accounts/Profile', blank=True)

    def __str__(self):
        return self.user.username
