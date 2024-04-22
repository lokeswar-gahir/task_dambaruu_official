from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    def __init__(self, *args, **kwargs):
        super(AdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
    class Meta:
        model = Admin
        fields = ['username', 'first_name', 'last_name', 'email','gender']


class DefaultUserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    def __init__(self, *args, **kwargs):
        super(DefaultUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
    class Meta:
        model = DefaultUser
        fields = ['username', 'first_name', 'last_name', 'email', 'gender']


class SuperAdminRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    def __init__(self, *args, **kwargs):
        super(SuperAdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','gender']


class DefaultUserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(DefaultUserUpdateForm, self).__init__(*args, **kwargs)
            
            if self.instance.pk:
                self.fields['username'].widget.attrs['readonly'] = True
                self.fields['username'].widget.attrs['class'] = 'testing_class'
                # self.fields['username'].widget.attrs.update({'class': 'input-style'})
                self.fields['username'].help_text = ''
                # self.fields['email'].required = False
                # self.fields['email'].widget.attrs['readonly'] = True
                # self.fields['password'].widget.attrs['readonly'] = True
                # self.fields['password'].required = False

    class Meta:
        model = DefaultUser
        fields = ['username', 'first_name', 'last_name', 'email', 'type']


class AdminUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(AdminUpdateForm, self).__init__(*args, **kwargs)

            if self.instance.pk:
                self.fields['username'].widget.attrs['readonly'] = True
                self.fields['username'].help_text = ''

    class Meta:
        model = Admin
        fields = ['username', 'first_name', 'last_name', 'email', 'type']


class SuperAdminUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(SuperAdminUpdateForm, self).__init__(*args, **kwargs)
            if self.instance.pk:
                self.fields['username'].widget.attrs['readonly'] = True
                self.fields['username'].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'type']


     