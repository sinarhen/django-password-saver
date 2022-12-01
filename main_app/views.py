from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import PasswordSettingForm
from .passgen import generate


# Create your views here

@login_required
def index(request):
    password = 'YOUR PASSWORD'
    form = PasswordSettingForm()
    if request.method == 'POST':
        form = PasswordSettingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            digits = cd['digits']
            spec_symbols = cd['special_symbols']
            letters = cd['letters']
            length = cd['length']
            password = generate(digits, spec_symbols, letters, length)
    return render(request, template_name='main_app/index.html', context={'form': form, 'password': password})

