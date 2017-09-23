from django.conf.urls import url, include
from django.contrib import admin
from . import views

# from account.views import register

app_name = 'account'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    ]
