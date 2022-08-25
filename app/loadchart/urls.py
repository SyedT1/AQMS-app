from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.showhome,name='load-home'),
    path('fun/',views.goto,name='loadchartfun'),
    path('barchart1/',views.index,name='barchart1'),
]