# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Questions(models.Model):

    question = models.CharField(max_length=100)
    publish_date = models.DateTimeField("Publish Date")

    def __str__(self):
        return self.question


class Choice(models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

