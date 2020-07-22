from django.urls import path
from core import views

app_name = 'user_profile'

urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('logout/', views.logout_user, name="logout"),
    path('login/', views.login_user, name="login")
]