from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def logout(request):
    """Logs out the user"""
    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Logs the user in"""
    return render(request, 'login.html')    

