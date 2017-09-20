from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=20, unique=True,
                                primary_key=True)
    email = models.EmailField(_('email address'), max_length=50, unique=True)
    first_name = models.CharField(_('first name'), max_length=20, blank=False)
    last_name = models.CharField(_('last name'), max_length=20, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user'
                                               ' can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user '
                                                'should be treated as '
                                                'active. Un-select this instead'
                                                ' of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    photo = models.ImageField(upload_to='profile_pics/')
    profile_url = models.URLField(blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
