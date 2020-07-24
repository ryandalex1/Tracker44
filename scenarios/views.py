from django.shortcuts import render


def expansion_list(request):
    return render(request, 'scenarios/expansion_list.html')


def all_scenarios(request):
    return render(request, 'scenarios/all_scenarios.html')

