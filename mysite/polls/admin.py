# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

# Register your models here.
from polls.models import Question
from .models import Project
admin.site.register(Project)
admin.site.register(Question)
