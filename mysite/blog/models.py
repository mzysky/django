# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('timestamp', )
