from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import datetime


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    suspended = models.BooleanField(default=1)

    @property
    def is_admin(self):
        return bool(self.administrator)

    def make_admin(self, admin):
        self.administrator = admin

    @property
    def date_joined(self):
        return self.user.date_joined

    @property
    def is_suspended(self):
        return bool(self.suspended)
