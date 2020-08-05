from django.shortcuts import render, get_object_or_404

from .models import Scenario, Expansion


def expansion_list(request):
    return render(request, 'scenarios/expansion_list.html')


def expansion_scenarios(request, expansion_abbreviation):
    if expansion_abbreviation == 'all':
        context = {'scenarios': Scenario.objects.all(), 'title': 'ALL SCENARIOS'}
    else:
        expansion = get_object_or_404(Expansion, abbreviation=expansion_abbreviation)
        context = {'scenarios': expansion.scenario_set.all(), 'title': expansion.name.upper()}
    return render(request, 'scenarios/scenario_list.html', context)
