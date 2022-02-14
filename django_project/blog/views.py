from django.shortcuts import render
from django.http import HttpResponse


posts = None

def home(request):
    my_context = {
        "posts": posts
    }
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")