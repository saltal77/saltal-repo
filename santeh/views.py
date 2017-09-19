# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import *

def main_view(request):
    info = AboutMe.objects.all()
    slogan1 = info[0].slogan1
    slogan2 = info[0].slogan2
    slogan3 = info[0].slogan3
    slogan4 = info[0].slogan4
    about = info[0].about

    return render(request, 'main.html', {'slogan1' : slogan1, 'slogan2' :
        slogan2, 'slogan3' : slogan3, 'slogan4' : slogan4, 'about' : about, 'info': info})


def about_view(request):

    return render(request, 'about.html')

def service_view(request):

    return render(request, 'service.html')

def discount_view(request):

    return render(request, 'discount.html')


def gallery_view(request):

    return render(request, 'gallery.html')


def interest_view(request):

    return render(request, 'interest.html')

def review_view(request):

    return render(request, 'review.html')



def contact_view(request):

    return render(request, 'contact.html')
