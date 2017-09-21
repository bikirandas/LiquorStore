from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from LiqourApp.views import read_file
from LiquorStore.settings import BASE_DIR
import os


def register(request):
    base_dir = BASE_DIR
    base_dir = os.path.join(base_dir, 'LiqourApp/static/appdata/menubar.txt')
    # print(base_dir)
    head_list = read_file(base_dir)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(str(form))
            form.save()
            return redirect(reverse('/register/'))
            # return render(request, 'registered.html', head_list)
    else:
        form = RegistrationForm()
        print(str(form))
        args = {'form': form}
        head_list.update(args)
        print(head_list)
        return render(request, 'registration.html', head_list)

