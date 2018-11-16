from django.forms import ModelForm, TextInput, EmailInput, DateInput, DateField, PasswordInput, ValidationError
from ..models import User, Role, Permission, UserProfile


class UserCreateForm(ModelForm):
    account_expiry_date = DateField(widget=DateInput(attrs={'class': 'input date-input'}), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'User Name'}),
            'password': PasswordInput(attrs={'class': 'input'})
        }

    def is_valid(self):

        # run parent validation first
        valid = super(UserCreateForm, self).is_valid()
        if not valid:
            return valid

        # check if username or email already exists
        try:
            user = User.objects.get(email=self.cleaned_data['email'])

            if user is not None:
                self.add_error('email', 'Email Already Exists!')
                return False

        # no user with this username or email address
        except User.DoesNotExist:
            pass

        return True

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'],
                                        self.cleaned_data['password'])
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.save()
        profile = UserProfile(user=user, account_expiry_date=self.cleaned_data['account_expiry_date'])
        profile.save()
        return user


class UserUpdateForm(ModelForm):
    account_expiry_date = DateField(widget=DateInput(attrs={'class': 'input date-input'}), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'User Name', 'readonly': 'readonly'})
        }

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit)
        profile = UserProfile.objects.get(user=user)
        expiry = self.cleaned_data['account_expiry_date']
        if profile.account_expiry_date != expiry:
            profile.account_expiry_date = expiry
            profile.save()
        return user


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class FeatureForm(ModelForm):
    class Meta:
        model = Permission
        fields = ['sysFeature']




