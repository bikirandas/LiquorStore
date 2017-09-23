from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='Delhi')


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='account/profile_image', blank=True)

    upm = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    # print(sender)
    if kwargs['created']:
        # UserProfile().objects.create(user=kwargs['instance'])
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        # UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
