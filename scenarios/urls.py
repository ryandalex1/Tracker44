from django.urls import path

import scenarios.views


app_name = 'scenarios'

urlpatterns = [
    # /scenarios/
    path('', scenarios.views.expansion_list, name='expansions'),
    # /scenarios/M44/
    # /scenarios/all/
    path('<expansion_abbreviation>/', scenarios.views.expansion_scenarios, name='expansion_scenarios')
]
