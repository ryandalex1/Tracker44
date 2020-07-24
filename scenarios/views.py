from django.shortcuts import render

from .models import Scenario


def expansion_list(request):
    return render(request, 'scenarios/expansion_list.html')


def all_scenarios(request):
    context = {'scenarios': Scenario.objects.all()}
    return render(request, 'scenarios/all_scenarios.html', context)

