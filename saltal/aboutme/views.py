from django.shortcuts import render, render_to_response
from datetime import date
from .models import AboutMe, MyLearning, MyJobs, Organizations

nodata = 'Контент редактируется...'

def about_view(response):

    dt = date(1977, 10, 1)
    info = AboutMe.objects.all()
    info1 = info[0].text1
    info2 = info[0].text2
    # info1 = []
    # info2 = []
    return render_to_response('about.html', {'info1': info1, 'info2': info2, 'date_birth': dt, 'nodata': nodata})

def jobs_view(response):

    jobs = MyJobs.objects.all()
    #jobs = []
    return render_to_response('jobs.html', {'jobs': jobs, 'nodata': nodata})

def learning_view(response):

    learns = MyLearning.objects.all()
    #learns = []
    return render_to_response('learning.html', {'learns': learns, 'nodata': nodata})


def job_info_view(response, pk):

    index = MyJobs.objects.filter(id=pk).values('orgname_id')
    index = index[0].get('orgname_id')
    firms = Organizations.objects.filter(id=index)
    #firms = []
    return render_to_response('jobinfo.html', {'firms': firms, 'nodata': nodata})
