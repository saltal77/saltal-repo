from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Info, Revw, Mark, Descript, MotoStories, MotoExploit, MotoCharacter

def site_view(request):

    info = Info.objects.all()
    marks = Mark.objects.all()
    query = request.GET.get('query')
    if query:
        info = info.filter(text__icontains=query)
    return render(request, 'index.html', {'info': info, 'marks': marks, 'query': query})

@login_required
def welcome_view(request):
    marks = Mark.objects.all()
    return render(request, 'welcome.html', {'marks': marks})

def character_view(request):
    marks = Mark.objects.all()
    motocharacter = MotoCharacter.objects.all()
    return render(request, 'character.html', {'marks': marks, 'motocharacter': motocharacter})

def exploit_view(request):
    marks = Mark.objects.all()
    motoexploit = MotoExploit.objects.all()
    return render(request, 'exploit.html', {'marks': marks, 'motoexploit': motoexploit})

def review_view(request):
    marks = Mark.objects.all()
    reviews = Revw.objects.all().order_by('-create_date')
    query = request.GET.get('query')
    if query:
        reviews = reviews.filter(text__icontains=query)
    paginator = Paginator(reviews, 2)
    page = request.GET.get('page')
    try:
        revws = paginator.page(page)
        #print(type(revws))
    except PageNotAnInteger:
        revws = paginator.page(1)
    except EmptyPage:
        revws = paginator.page(paginator.num_pages)
    return render(request, 'review.html', {'revws': revws, 'numbers': range(1, paginator.num_pages + 1), 'query': query, 'marks': marks})

def review_details(request, id):
    marks = Mark.objects.all()
    revw = get_object_or_404(Revw, id=id)
    return render(request, 'review-detail.html', {'revw': revw, 'marks': marks})

def marks_view(request, mark_id):
    descr = Descript.objects.filter(mark_id=mark_id)
    marks = Mark.objects.all()
    return render(request, 'marks.html', {'descr': descr, 'marks': marks})

def motohistory_view(request):
    marks = Mark.objects.all()
    stories = MotoStories.objects.all()
    return render(request, 'motohistory.html', {'marks': marks, 'stories': stories})

def login(request):

    info = Info.objects.all()
    if request.method == 'POST':
        #print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/welcome/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True, 'info': info})
    raise Http404

def logout(request):

    auth.logout(request)
    return HttpResponseRedirect("/")
