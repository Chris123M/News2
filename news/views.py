from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("News<br>example story<br> 07/04/2020")

def headline(request):
    return HttpResponse("Headline")



