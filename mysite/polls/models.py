# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Project(models.Model):
    p_name = models.CharField(max_length=100)
    p_manager = models.CharField(max_length=100)
    p_desc = models.CharField(max_length=1000)
    p_start = models.DateField('date published')
    p_end = models.DateField('date terminated')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



#password : 19960501wagh