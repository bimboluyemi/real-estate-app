from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from ..models import UserProfile, User
from ..forms.access_control_forms import  UserCreateForm, UserUpdateForm
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class UserList(ListView):
    model = UserProfile
    template_name = 'manage_users/list.html'
    context_object_name = 'users'
    # queryset = User.objects.filter(is_staff=False)


class UserCreate(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'manage_users/user.html'
    success_url = reverse_lazy('system-admin:users')

    def get_success_url(self):
        return self.success_url


class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'manage_users/user.html'
    success_url = '/system-admin/users'

    def get_form(self, form_class=form_class):
        form = super(UserUpdate, self).get_form(form_class)
        username = form.instance.username
        profile = UserProfile.objects.get(user__username=username)
        form.fields['account_expiry_date'].initial = profile.account_expiry_date
        return form


class UserDelete(DeleteView):
    model = User
    template_name = 'manage_users/delete.html'
    success_url = '/system-admin/users'


class UserEnable(FormView):
    template_name = 'manage_users/enable.html'

    # def get_initial(self):


def assign_role(request, user_id):

    return render(request, 'manage_users/assign_role.html')


