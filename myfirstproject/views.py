from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Lenia')

def home(request):
    return render(request,'home.html',{'greeting':'hello'})