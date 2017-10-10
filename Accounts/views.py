from django.shortcuts import render, redirect, render_to_response
from .forms import RegistrationForm, UserProfileForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from LiqourApp.views import read_file
from LiquorStore.settings import BASE_DIR
import os
from .models import UserProfile
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
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
    params = {}
    params.update(csrf(request))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Django's built-in authentication function:
            print(username, password)
            user = authenticate(username=username, password=password)
            print('after aunthenticate', user)
        # If we have a user
            if user is not None:
                # Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, username)
                    # Send the user back to some page.
                    request.session['username'] = user
                    # In this case their homepage.
                    # return HttpResponseRedirect(reverse('/home/'))
                    args = {'user': username}
                    head_list.update(args)
                    return render(request, 'user_profile.html', head_list)
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return HttpResponse("Invalid login details supplied.")

    else:
        form = LoginForm()
        args = {'form': form}
        head_list.update(args)
        # Nothing has been provided for username or password.
        return render(request, 'login.html', head_list)


@login_required()
def user_profile(request):
    logon = True
    user = request.session.get('username')
    print(user)
    args = {'username': user, 'logon': logon}
    head_list.update(args)
    return render(request, 'user_profile.html', head_list)
