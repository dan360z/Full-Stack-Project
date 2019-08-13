from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm

# Create your views here.
def logout(request):
    """Logs out the user"""
    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Logs the user in"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})    

