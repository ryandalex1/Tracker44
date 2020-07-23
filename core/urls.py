from django.urls import path

from . import views

urlpatterns = [
    # /core/
    path('', views.index, name='index'),
]
