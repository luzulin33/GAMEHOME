from django.shortcuts import render
from .forms import UserCreationForm
# Create your views here.
def register(request):
    userForm = UserCreationForm()
    return render(request, 'user/register.html',locals())