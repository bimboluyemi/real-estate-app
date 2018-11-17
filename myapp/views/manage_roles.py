from django.shortcuts import render, get_object_or_404, redirect
from ..models import Role, RolePermission
from django.http import HttpResponseRedirect
from ..forms.access_control_forms import RoleForm, ManagePermissionForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


def all_roles(request):
    return render(request, 'manage_roles/list.html',
                  {'title': 'Manage Roles',
                   'roles': Role.objects.all()})


def role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return redirect('system-admin:roles')
    else:
        form = RoleForm(instance=r)
    return render(request, 'manage_roles/role.html',
                  {'title': 'Add Role',
                   'form': form})


class ManagePermission(FormView):
    template_name = 'manage_roles/manage_permission.html'
    success_url = '/system-admin/roles'

    def get(self, request, *args, **kwargs):
        role = Role.objects.get(pk=self.kwargs['pk'])
        role_permissions = RolePermission.objects.filter(role=role)
        form = ManagePermissionForm(initial={'features': [a.permission_id for a in role_permissions]}) \
            if any(role_permissions) else ManagePermissionForm()
        return render(request, self.template_name, {'role': role, 'form': form})

    def post(self, request, *args, **kwargs):
        role = Role.objects.get(pk=self.kwargs['pk'])
        form = ManagePermissionForm(request.POST)
        selected_features = request.POST.getlist('features')
        form.save(role, selected_features)
        return HttpResponseRedirect(self.success_url)


class RoleDelete(DeleteView):
    model = Role
    template_name = 'manage_roles/delete.html'
    success_url = '/system-admin/roles'
