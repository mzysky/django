# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from datetime import datetime
from blog.models import BlogPost
from django.http import HttpResponse
def archive(request):
    posts = BlogPost.objects.all().order_by("title") #order the data
    return render_to_response("archive.html", {'posts':posts})
