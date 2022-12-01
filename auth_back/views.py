from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django import conf


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                username = cd['username']
                password = cd['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(conf.settings.LOGIN_REDIRECT_URL)
        return render(request, template_name='auth_back/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect(conf.settings.LOGIN_REDIRECT_URL)

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    return render(request, template_name='auth_back/register.html', context={'form': form})
