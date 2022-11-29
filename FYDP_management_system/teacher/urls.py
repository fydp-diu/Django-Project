from django.urls import path
from . import views
urlpatterns = [
    path('t_home/', views.t_home,name='t_home'),
    

]