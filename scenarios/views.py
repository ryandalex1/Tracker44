from django.shortcuts import render, get_object_or_404

from .models import Scenario, Expansion


def expansion_list(request):
    return render(request, 'scenarios/expansion_list.html')


def all_scenarios(request):
    context = {'scenarios': Scenario.objects.all()}
    return render(request, 'scenarios/all_scenarios.html', context)


def expansion_scenarios(request, expansion_abbreviation):
    expansion = get_object_or_404(Expansion, abbreviation=expansion_abbreviation)
    context = {'scenarios': expansion.scenario_set.all()}
    return render(request, 'scenarios/all_scenarios.html', context)
