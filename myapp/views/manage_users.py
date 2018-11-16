from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from ..models import UserProfile, User
from ..forms.access_control_forms import UserForm
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class UserList(ListView):
    model = UserProfile
    template_name = 'manage_users/list.html'
    context_object_name = 'users'
    # queryset = User.objects.filter(is_staff=False)


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'manage_users/user.html'
    success_url = '/system-admin/users'

    def form_valid(self, form):
        m = form.save()
        account_expiry = form.cleaned_data['account_expiry_date']
        u = UserProfile(user=m, account_expiry_date=account_expiry)
        u.save()
        return HttpResponseRedirect(self.success_url)


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'manage_users/user.html'
    success_url = '/system-admin/users'


class UserDelete(DeleteView):
    model = User
    template_name = 'manage_users/delete.html'
    success_url = '/system-admin/users'


class UserEnable(FormView):
    template_name = 'manage_users/enable.html'

    # def get_initial(self):


def assign_role(request, user_id):

    return render(request, 'manage_users/assign_role.html')


