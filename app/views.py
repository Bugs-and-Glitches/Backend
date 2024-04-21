from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return  render(request ,'index.html')


def Login(request):
    return  render(request ,'auth/login.html')

def Register(request):
    return  render(request ,'auth/register.html')