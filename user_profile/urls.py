from django.urls import path

import user_profile.views


app_name = 'user_profile'

urlpatterns = [
    # /user_profile/sign_up
    path('sign_up/', user_profile.views.sign_up, name="sign_up"),
    # /user_profile/logout
    path('logout/', user_profile.views.logout_user, name="logout"),
    # /user_profile/login
    path('login/', user_profile.views.login_user, name="login"),
    # /user_profile/profile
    path('profile/', user_profile.views.profile, name="profile")
]
