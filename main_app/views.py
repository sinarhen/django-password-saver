from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import PasswordSettingForm
from .passgen import generate
from .models import Password


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
            if request.POST.get('save') == 'true':
                Password.objects.create(password=password, owner=request.user)

    return render(request, template_name='main_app/index.html',
                  context={'form': form, 'password': password, 'saved': Password.objects.filter(owner=request.user)})


@login_required
@require_POST
def save(request):
    print(request.POST)
    Password.objects.create(password=request.POST.get('result'), owner=request.user)
    return redirect('main:index')


@login_required
@require_POST
def delete(request):
    Password.objects.delete(password=request.POST.get('delete_password'), owner=request.user)
    return redirect('main:index')
