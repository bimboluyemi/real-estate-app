from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from ..models import User
from ..forms.access_control_forms import UserForm


def all_users(request):
    data = {
        'title': 'Manage Users',
        'users': User.objects.all()
    }
    return render(request, 'manage_users/list.html', data)


def user(request, user_id=None):
    u = User()
    if user_id is not None:
        u = get_object_or_404(User, id=user_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST, instance=u)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/system-admin/users')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm(instance=u)

    data = {
        'title': 'Create New User',
        'form': form
    }
    return render(request, 'manage_users/user.html', data)


def assign_role(request, user_id):
    return render(request, 'manage_users/assign_role.html')


def delete_user(request, user_id):
    return 200
