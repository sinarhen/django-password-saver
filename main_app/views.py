from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here

@login_required
def index(request):
    return render(request, template_name='main_app/index.html', context={})


