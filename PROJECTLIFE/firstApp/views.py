from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    context = {"data": "WELCOME TO THE HOME PAGE"}
    return render(response, 'home.html', context)

def about(response):
    context = {"data": "WELCOME TO THE ABOUT PAGE"}
    return render(response, 'about.html', context)

def contact(response):
    context = {"data": "WELCOME TO THE CONTACT PAGE"}
    return render(response, 'contact.html', context)


    

