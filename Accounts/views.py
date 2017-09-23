from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from LiqourApp.views import read_file
from LiquorStore.settings import BASE_DIR
import os
from .models import UserProfile


def register(request):
    registered = False
    fp = os.path.join(BASE_DIR, 'LiqourApp\static\\appdata\menubar.txt')
    head_list = read_file(fp)
    if request.method == 'POST':
        reg_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if reg_form.is_valid() and profile_form.is_valid():
            user = reg_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            args = {'reg_form': reg_form, 'profile_form': profile_form, 'registered': True}
            head_list.update(args)
            return render(request, 'registration.html', head_list)
        else:
            print(reg_form.errors, profile_form.errors)
            args = {'reg_form': reg_form.errors, 'profile_form': profile_form.errors}
            head_list.update(args)
            return render(request, 'registration.html', head_list, args)
    else:
        reg_form = RegistrationForm()
        profile_form = UserProfileForm()
        args = {'reg_form': reg_form, 'profile_form': profile_form}
        head_list.update(args)
        return render(request, 'registration.html', head_list)
