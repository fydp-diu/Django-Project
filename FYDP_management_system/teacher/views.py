from django.shortcuts import render,HttpResponse

# Create your views here.
def t_home(request):
    return render(request,'teacher/t_home.html')
