from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registration.html', args)

