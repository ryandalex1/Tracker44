from django.urls import path

import scenarios.views


app_name = 'scenarios'

urlpatterns = [
    # /scenarios/
    path('', scenarios.views.expansion_list, name='expansions'),
]
