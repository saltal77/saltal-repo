# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, render_to_response
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.conf import settings
#from django.template import Context
#from django.template.loader import get_template
#from django.template import RequestContext
#from django.views.generic.edit import CreateView
#from django.template.context_processors import csrf
#from django.core.mail import send_mail


def main_view(request):
    info = AboutMe.objects.all()
    slogan1 = info[0].slogan1
    slogan2 = info[0].slogan2
    slogan3 = info[0].slogan3
    slogan4 = info[0].slogan4
    about = info[0].about
    portfolio = MainPageWorks.objects.all().order_by('-date')[:6]
    return render(request, 'main.html', {'slogan1' : slogan1, 'slogan2' :
        slogan2, 'slogan3' : slogan3, 'slogan4' : slogan4, 'about' : about, 'portfolio' : portfolio})


def sender_mail(theme, text):
	msg=EmailMessage(theme, text, settings.SERVER_EMAIL, [settings.MASTER_EMAIL])
	msg.content_subtype = 'html'
	msg.send()


def about_view(request):
    return render(request, 'about.html')


def service_view(request):
    services = Service.objects.all().order_by('title')
    return render(request, 'service.html', {'services' : services})


def discount_view(request):
    discounts = Discount.objects.all().order_by('-date')
    return render(request, 'discount.html', {'discounts' : discounts})


def gallery_view(request):
    portfolio = MainPageWorks.objects.all().order_by('-date')
    return render(request, 'gallery.html', {'portfolio' : portfolio })


def interest_view(request):
    interests = Interest.objects.all().order_by('-date')
    return render(request, 'interest.html', {'interests' : interests})


def review_view(request):
    comments = Comment.objects.all().order_by('-date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            author = request.POST['author']
            text = request.POST['text']
            if request.POST['town']:
                town = request.POST['town']
                town = u' из г.' + town
            else:
                town =''
            fmail = u'от: %s.  Отзыв: %s %s. Напоминание: необходимо разрешить показывать этот отзыв на сайте или удалить...' \
                    % (author.title(), text.capitalize(), town)
            theme = u'Оставлен новый отзыв по работам от пользователя %s.' % author.title()
            sender_mail(theme, fmail)
            comment.save()
            return render(request, 'success.html', {'author' : author})
    else:
        form = CommentForm()
    return render(request, 'review.html', {'comments' : comments , 'form': form } )



def contact_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            name = request.POST['name']
            email = request.POST['email']
            text = request.POST['text']
            if request.POST['tlf']:
                tlf = request.POST['tlf']
                tlf = u' т.' + tlf
            else:
                tlf = u"Телефона не осталено."
            email = "<a href='mailto:%s'>%s</a>" % (email, email)

            fmail = u'от:  %s.  Вопрос/Заявка:  %s, контакты: %s   %s' \
                    % (name.title(), text.capitalize(), email, tlf)
            theme = u'Поступила новая заявка или вопрос с сайта от пользователя %s.' % name.title()
            sender_mail(theme, fmail)
            order.save()
            return render(request, 'success.html', {'name': name })
    else:
        form = OrderForm()
    return render(request, 'contact.html',  {'form': form})


# def page_not_found(request):
#     response = render_to_response('404.html',context_instance=RequestContext(request))
#     response.status_code = 404
#     return response

# def server_error(request):
#     response = render_to_response('500.html',context_instance=RequestContext(request))
#     response.status_code = 500
#     return response