# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from datetime import datetime
from blog.models import BlogPost
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
def archive(request):
    posts = BlogPost.objects.all().order_by("-title") #order the data
    return render(request, "archive.html", {'posts':posts})
def create_blogpost(request):
    print "***************"
    if request.method == 'POST':
        BlogPost(
                title = request.POST.get('title'),
                body = request.POST.get('body'),
                timestamp = datetime.now(),
                ).save()
    return HttpResponseRedirect('/blog/')

