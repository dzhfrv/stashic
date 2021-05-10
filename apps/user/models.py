from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    date_added = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(_('first name'), max_length=20, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=20, blank=True)
    second_name = models.CharField(_('second name'), max_length=20, blank=True)
    phone = models.CharField(_('phone'), max_length=12, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
