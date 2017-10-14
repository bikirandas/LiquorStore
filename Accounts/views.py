from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import RegistrationForm, UserProfileForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from LiqourApp.views import read_file
from LiquorStore.settings import BASE_DIR
import os
# from .models import UserProfile
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext
# from django.contrib.auth.hashers import make_password

fp = os.path.join(BASE_DIR, 'LiqourApp\static\\appdata\menubar.txt')
head_list = read_file(fp)


def register(request):
    registered = False
    if request.method == 'POST':
        reg_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if reg_form.is_valid() and profile_form.is_valid():
            user = reg_form.save()
            # print('before set password = ', user.password)
            # user.set_password(user.password)
            # print('after set password = ', user.password)
            user.save()
            print(user.password)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                print('uploading pic .....')
            profile.save()
            args = {'reg_form': reg_form, 'profile_form': profile_form, 'registered': True}
            head_list.update(args)
            return render(request, 'registration.html', head_list)

        else:
            print(reg_form.errors, profile_form.errors)
            args = {'reg_form': reg_form.errors, 'profile_form': profile_form.errors, 'registered': False}
            head_list.update(args)
            return render(request, 'registration.html', head_list, args)
    else:
        reg_form = RegistrationForm()
        profile_form = UserProfileForm()
        args = {'reg_form': reg_form, 'profile_form': profile_form, 'registered': False}
        head_list.update(args)
        print(head_list)
        return render(request, 'registration.html', head_list)


def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        print(request.user.is_authenticated)
    args = {'form': form}
    head_list.update(args)
    return render(request, 'login.html', head_list)


def logout(request):
    logout(request)


@login_required(login_url='/accounts/login/')
def user_profile(request):
    logon = True
    # user = request.user
    # print(str(user))
    args = {'logon': logon}
    head_list.update(args)
    return render(request, 'user_profile.html', head_list)
