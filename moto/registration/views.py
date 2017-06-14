from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from amsite.models import Info, Revw, Mark, Descript

def registration(request):

    marks = Mark.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/welcome/')
        context = {'form': form, 'marks': marks}
        return render(request, 'registration.html', context)
    context = {'form': RegistrationForm(),  'marks': marks}
    return render(request, 'registration.html', context)
