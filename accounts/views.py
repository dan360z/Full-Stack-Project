from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, RegistrationForm
from django.contrib.auth.models import User

@login_required
def logout(request):
    """Logs out the user"""
    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Renders the login form page and logs the user in if the user is valid"""

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


def registration(request):
    """Render the registration page and registers a new user"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else: 
                messages.error(request, "Unable to register your account at this time")                        

    else:                         
        registration_form = RegistrationForm()

    return render(request, 'registration.html', {"registration_form": registration_form})

@login_required
def user_profile(request):
    """This renders the user's profile page"""
    user = User.objects.get(email=request.user.email)
    username = user.username.capitalize()
    return render(request, 'profile.html', {"profile": user, "username": username})
