from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import PasswordSettingForm
from .passgen import generate
from .models import Password


# Create your views here

@login_required
def index(request):
    default_password = 'YOUR_PASSWORD'
    form = PasswordSettingForm()
    if request.method == 'POST':
        password_post_get = request.POST.get("password")
        if request.POST.get('save') == 'true' and password_post_get != 'YOUR_PASSWORD':
            default_password = password_post_get
            return redirect('main:save', password_post_get)
        else:
            form = PasswordSettingForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                digits = cd['digits']
                spec_symbols = cd['special_symbols']
                letters = cd['letters']
                length = cd['length']
                default_password = generate(digits, spec_symbols, letters, length)

    return render(request, template_name='main_app/index.html',
                  context={'form': form,
                           'password': default_password,
                           'saved': Password.objects.filter(owner=request.user)})


@login_required
def save(request, password):
    Password.objects.create(password=password, owner=request.user)
    return redirect('main:index')


@login_required
def delete(request, pk):
    Password.objects.get(pk=pk).delete()
    return redirect('main:index')
