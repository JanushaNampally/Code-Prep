from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
def simplex_method(request):
    if request.method == 'POST':
        equations = request.POST.get('equations')
        solution = "Steps to solve simplex method based on equations provided."
        return JsonResponse({'solution': solution})
    return render(request, 'simplex.html')


def graphical_method(request):
    if request.method == 'POST':
        equations = request.POST.get('equations')
        solution = "Steps to solve Graphical method based on equations provided"
        return JsonResponse({'solution': solution})
    return render(request, 'graphical.html')

def transportation_method(request):
    if request.method == 'POST':
        equations = request.POST.get('equations')
        solution = "Steps to solve transportation method based on equations provided"
        return JsonResponse({'solution': solution})
    return render(request, 'transportation.html')

def home(request):
    return render(request, 'home.html')

