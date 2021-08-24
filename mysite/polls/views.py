from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dave(request):
    return HttpResponse("this is my own view")

def newtest(request):
    return HttpResponse("Last test of routing")
