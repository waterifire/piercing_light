from django.shortcuts import render

# Create your views here.

def dg_home(request):
    context = {}
    return render(request, 'dg/dg_home.html', context)

def dg_add(request):
    context = {}
    return render(request, 'dg/dg_add.html', context)
