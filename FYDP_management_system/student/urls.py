from django.urls import path
from . import views
urlpatterns = [
    path('s_home/', views.s_home,name='s_home'),
    path('s_profile/', views.s_profile,name='s_profile'),
    path('supervisor/', views.supervisor,name='supervisor'),
    path('s_logout/', views.s_logout,name='s_logout'),
]