from django.shortcuts import render, redirect
from django.contrib.auth import login

from user_profile.forms import SignUpForm


def index(request):
    return render(request, 'core/index.html')


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)
