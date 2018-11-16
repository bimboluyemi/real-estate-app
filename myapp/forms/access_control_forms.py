from django.forms import ModelForm, TextInput, EmailInput, DateInput, DateField
from ..models import User, Role, Permission, UserProfile


class UserForm(ModelForm):
    account_expiry_date = DateField(widget=DateInput(attrs={'class': 'input date-input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'User Name'}),
        }


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class FeatureForm(ModelForm):
    class Meta:
        model = Permission
        fields = ['sysFeature']




