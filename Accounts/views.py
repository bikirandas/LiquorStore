from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from LiqourApp.views import read_file
from LiquorStore.settings import BASE_DIR
import os


def register(request):
    registered = False
    fp = os.path.join(BASE_DIR, 'LiqourApp\static\\appdata\menubar.txt')
    print(BASE_DIR)
    head_list = read_file(fp)
    print(head_list)
    if request.method == 'POST':
        reg_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if reg_form.is_valid() and profile_form.is_valid():
            user = reg_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            args = {'reg_form': reg_form, 'profile_form': profile_form}
            head_list.update(args)
            registered = True
        else:
            print(reg_form.errors, profile_form.errors)
    else:
        reg_form = RegistrationForm()
        profile_form = UserProfileForm()
        args = {'reg_form': reg_form, 'profile_form': profile_form}
        head_list.update(args)
    return render(request, 'registration.html', head_list)
