from django.http import HttpResponse
from django.shortcuts import render

def greet(request, name):
    context = {
        "name": name.capitalize()
    }
    return render(request, "hello/index.html", context)
