# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city="Berlin")

class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to="profile_image", blank=True)

    berlin = UserProfileManager()

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        db_table = 'user_profiles'

def create_profile(sender, **kwargs):
    if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs["instance"])

post_save.connect(create_profile, sender=User)
