from django.shortcuts import render_to_response, render
# from django import forms
# from django.http import HttpResponse
from LiqourApp.apps import Locate
# from django.views.generic import View
import os, ast


# def index(request):
#     city = City.objects.all()
#     t = loader.get_template("__header.html")
#     return HttpResponse(t.render())


def index(request):
    head_list = read_file('static/appdata/menubar.txt')
    # loc = Locate.find_you('this user')
    # print(head_list, loc)
    return render_to_response('__header.html', head_list)


def home(request):
    head_list = read_file('static/appdata/menubar.txt')
    return render(request, 'home.html', head_list)


def location_view(request):
    head_list = read_file('static/appdata/menubar.txt')
    return render(request, 'location.html', head_list)


def register(request):
    head_list = read_file('static/appdata/menubar.txt')
    return render(request, 'registration.html', head_list)


def read_file(file_name):
    menu_list = []
    head_list = {}
    fp = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.join(fp, file_name)
    with open(fp, 'r') as mb:
        for i, line in enumerate(mb):
            menu_list.append(line)
            hl = ast.literal_eval(menu_list[i])
            head_list.update(hl)

    print(head_list)
    return head_list
