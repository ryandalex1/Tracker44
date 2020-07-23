from django.shortcuts import render


def expansion_list(request):
    return render(request, 'scenarios/expansion_list.html')
