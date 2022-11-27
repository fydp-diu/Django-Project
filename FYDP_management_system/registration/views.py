from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return render(request,'registration/home.html')
def registration(request):
    return render(request,'registration/home.html')
def t_registration(request):
    return render(request,'registration/home.html')
def s_registration(request):
    return render(request,'registration/home.html')
def t_login(request):
    return render(request,'registration/home.html')
def s_login(request):
    return render(request,'registration/home.html')
