from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def t_home(request):
    return render(request,'teacher/t_home.html')
def student_list(request):
    return render(request,'teacher/student_list.html')
def work_area(request):
    return render(request,'teacher/work_area.html')
def t_profile(request):
    return render(request,'teacher/t_profile.html')
def t_logout(request):
    logout(request)
    return redirect('t_login')
