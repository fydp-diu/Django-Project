from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from student.models import S_Profile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model=S_Profile
        exclude=('user',)