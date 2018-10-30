from django.forms import ModelForm
from ..models import User, Role, Permission


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class FeatureForm(ModelForm):
    class Meta:
        model = Permission
        fields = ['sysFeature']

