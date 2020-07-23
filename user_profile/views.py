from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from user_profile.forms import SignUpForm


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


def logout_user(request):
    logout(request)
    return redirect("index")


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

    context = {}
    form = AuthenticationForm()
    context['form'] = form
    return render(request, "registration/login.html", context)
