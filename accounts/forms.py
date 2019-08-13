from django import forms

class UserLoginForm(forms.Form):
    """User login form"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)