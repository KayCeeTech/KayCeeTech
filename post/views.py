from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("cohort13")


def greet(request):
    return HttpResponse("greet")


def come(request):
    return HttpResponse("come")


def creat(request):
    return render(request, "htmlTag.html")
