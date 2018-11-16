from django.shortcuts import render, get_object_or_404, redirect
from ..models import Role
from ..forms.access_control_forms import RoleForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


def all_roles(request):
    return render(request, 'manage_roles/list.html',
                  {'title': 'Manage Roles',
                   'roles': Role.objects.all()})


def role(request, role_id=None):
    r = Role()
    if role_id is not None:
        r = get_object_or_404(Role, id=role_id)
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


def delete_role(request):
    return 200


class RoleDelete(DeleteView):
    model = Role
    template_name = 'manage_roles/delete.html'
    success_url = '/system-admin/roles'
