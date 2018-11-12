from django.forms import ModelForm, TextInput, EmailInput
from ..models import User, Role, Permission


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
        }


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class FeatureForm(ModelForm):
    class Meta:
        model = Permission
        fields = ['sysFeature']




