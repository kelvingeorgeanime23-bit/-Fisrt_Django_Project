from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, 'main.html')

def about(response):
    return render(response, 'about.html')

