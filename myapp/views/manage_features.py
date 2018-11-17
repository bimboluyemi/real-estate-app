from django.shortcuts import render, redirect
from ..models import Permission
from ..forms.access_control_forms import FeatureForm
from django.views.generic import DeleteView


def all_features(request):
    return render(request, 'manage_features/list.html',
                  {'title': 'Manage System Features',
                   'features': Permission.objects.all()})


def feature(request):
    p = Permission()
    if request.method == 'POST':
        form = FeatureForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('system-admin:features')
    else:
        form = FeatureForm(instance=p)
    return render(request, 'manage_features/feature.html',
                  {'title': 'Add Feature',
                   'form': form})


class FeatureDelete(DeleteView):
    model = Permission
    template_name = 'manage_features/delete.html'
    success_url = '/system-admin/features'
