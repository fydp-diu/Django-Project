from django.urls import path
from . import views
urlpatterns = [
        path('dashboard/', views.dashboard),
        path('registration/', views.dashboard),
        path('t_registration/', views.dashboard),
        path('s_registration/', views.dashboard),
        path('t_login/', views.dashboard),
        path('s_login/', views.dashboard),



]