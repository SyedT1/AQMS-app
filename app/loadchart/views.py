from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def act(request):
    name = ['Sarah','Kala','mala']
    context = {
        'lsNames':name
    }
    return render(request,'loadchart/about.html',context)