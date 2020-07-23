from django.urls import path

import user_profile.views


app_name = 'user_profile'

urlpatterns = [
    path('sign_up/', user_profile.views.sign_up, name="sign_up"),
    path('logout/', user_profile.views.logout_user, name="logout"),
    path('login/', user_profile.views.login_user, name="login")
]