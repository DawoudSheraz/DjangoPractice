# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField(default=0, primary_key=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Skills(models.Model):

    title = models.CharField(max_length=20)
    users = models.ManyToManyField(UserProfile, related_name='user_skills')

    def __str__(self):
        return self.title
