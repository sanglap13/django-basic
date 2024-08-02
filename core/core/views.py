from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("Hello World, this is home")
    return render(req, "website/index.html")

def about(req):
    return HttpResponse("Hello World, this is about")

def contact(req):
    return HttpResponse("Hello World, this is contact")