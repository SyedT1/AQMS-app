from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def act(request):
    name = ['Sarah','Kala','mala']
    context = {
        'lsNames':name
    }
    return render(request,'loadchart/about.html',context)


def goto(request):
    dwell = request.GET["country"]
    context = {
        'country':dwell
    }
    return render(request,'loadchart/something.html',context)