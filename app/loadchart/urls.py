from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.act,name='loadchart-home'),
    path('fun/',views.goto,name='loadchartfun'),
]