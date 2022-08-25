from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.addAQI,name='addAQI-home'),
    path('ty/',views.showpage,name='addAQI-load'),
]