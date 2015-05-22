from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import datetime


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    customer_id = models.CharField(max_length=25, default='123456789')
    api_key = models.CharField(max_length=32, default='123456789')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    suspended = models.BooleanField(default=1)

    @property
    def date_joined(self):
        return self.user.date_joined

    @property
    def is_suspended(self):
        return bool(self.suspended)


class UserGroup(models.Model):
    group = models.OneToOneField(Group)

    @property
    def user_set(self):
        return self.group.user_set

    def __str__(self):
        return self.group.name


class ScoreHistory(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
