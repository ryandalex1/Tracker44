from django.urls import path

import scenarios.views


app_name = 'scenarios'

urlpatterns = [
    # /scenarios/
    path('', scenarios.views.expansion_list, name='expansions'),
    # /scenarios/all/
    path('all/', scenarios.views.all_scenarios, name='all_scenarios'),
    # /scenarios/M44/
    path('<expansion_abbreviation>/', scenarios.views.expansion_scenarios, name='expansion_scenarios')
]
