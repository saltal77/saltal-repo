# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404


def main_view(request):

    return render(request, 'main.html')

def about_view(request):

    return render(request, 'about.html')

def service_view(request):

    return render(request, 'service.html')

def gallery_view(request):

    return render(request, 'gallery.html')


def interest_view(request):

    return render(request, 'interest.html')

def review_view(request):

    return render(request, 'review.html')



def contact_view(request):

    return render(request, 'contact.html')
