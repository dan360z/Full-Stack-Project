from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm


def logout(request):
    """Logs out the user"""
    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Logs the user in"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect!")                            

    else:
        login_form = UserLoginForm() 

    return render(request, 'login.html', {"login_form": login_form})

