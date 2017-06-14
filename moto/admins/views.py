from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from registration.forms import RegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
#from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from .forms import InfoForm, RevwForm, MarkForm
from amsite.models import Info, Revw, Mark, Descript




#@user_passes_test(lambda u: u.is_superuser)
#@staff_member_required
@user_passes_test(lambda u: u.is_staff)
def admins_work(request):

    users = User.objects.all()
    user_form = RegistrationForm()
    return render(request, 'admins.html', {'users': users, 'form': user_form})

@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admins/')

@user_passes_test(lambda u: u.is_staff)
def create_user(request, user_id=None):

    if request.is_ajax():
        #print('user_id = ', user_id)
        if not user_id:
            #print('Not user_id')
            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users-list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404

@user_passes_test(lambda u: u.is_staff)
def get_user_form(request, user_id):

    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = RegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-register-form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

# def admin_review(request):
#     revws = Revw.objects.all()
#     return render(request, 'admins-review.html', {'revws': revws})


class AdminReview(ListView):
    model = Revw
    template_name = 'admins-review.html'
    context_object_name = 'revws'
    paginate_by = 4


# def admin_review_create(request):
#     if request.method == 'POST':
#         form = RevwForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/admins/review/')
#         context = {'form': form}
#         return render(request, 'admins-review-create.html', context)
#     context = {'form': RevwForm()}
#     return render(request, 'admins-review-create.html', context)


class AdminReviewCreate(CreateView):
    model = Revw
    template_name = 'admins-review-create.html'
    success_url = '/admins/review/'
    fields = ('__all__')
    context_object_name = 'form'


# def admin_review_delete(request, id):
#     if request.method == 'POST':
#         revw = get_object_or_404(Revw, id=id)
#         revw.delete()
#         return HttpResponseRedirect('/admins/review/')
#     raise Http404

class AdminReviewDelete(DeleteView):
    model = Revw
    context_object_name = 'revw'
    success_url = '/admins/review/'
    template_name = 'admins-confirm-delete.html'



# def admin_review_update(request, id):
#     revw = get_object_or_404(Revw, id=id)
#     if request.method == 'POST':
#         form = RevwForm(request.POST, instance=revw, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/admins/review/')
#         context = {'form': form}
#         return render(request, 'admins-review-update.html', context)
#     context = {'form': RevwForm(instance=revw)}
#     return render(request, 'admins-review-update.html', context)

class AdminReviewUpdate(UpdateView):
    model = Revw
    template_name = 'admins-review-update.html'
    fields = ('__all__')
    success_url = '/admins/review/'
    context_object_name = 'form'


# def admin_review_detail(request, id):
#     revw = get_object_or_404(Revw, id=id)
#     return render(request, 'admins-review-detail.html', {'revw': revw})

class AdminReviewDetail(DetailView):
    model = Revw
    template_name = 'admins-review-detail.html'
    context_object_name = 'revw'