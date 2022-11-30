from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def s_home(request):
    return render(request,'student/s_home.html')
def s_profile(request):
    return render(request,'student/s_profile.html')
def supervisor(request):
    return render(request,'student/supervisor.html')

def s_logout(request):
    logout(request)
    return redirect('s_login')