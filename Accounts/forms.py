from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (authenticate, get_user_model)

user_crrnt = get_user_model()


class RegistrationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email')

    # Remove help text from registration form
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This User Doesnot Exists")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError("This is user is not active.")
        return super(LoginForm, self).clean(*args, **kwargs)
