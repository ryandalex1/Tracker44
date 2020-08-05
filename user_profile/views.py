from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from user_profile.forms import SignUpForm
from user_profile.models import UserProfile


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
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


def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_profile:login')
    else:
        return render(request, "profile.html", {'profile': UserProfile.objects.get(user=request.user)})


def log_play(request):
    if not request.user.is_authenticated:
        return redirect('user_profile:login')
    else:
        return render(request, "play_entry.html")
