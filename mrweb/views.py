from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'mrweb/home.html')


def about(request):
    return render(request, 'mrweb/about.html')


def courses(request):
    return render(request, 'mrweb/courses.html')


def contact(request):
    return render(request, 'mrweb/contact.html')
