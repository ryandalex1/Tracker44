from django.urls import path
from core import views

urlpatterns = [
    path('sign_up/', views.sign_up, name="sign-up")
]