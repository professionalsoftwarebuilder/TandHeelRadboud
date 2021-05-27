from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import forms


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('mijnApp:index')
    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
