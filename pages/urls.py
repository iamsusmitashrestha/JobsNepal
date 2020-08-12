from django.urls import path
from . import views

urlpatterns = [
    # second parameter is the method we want to connect this to in the views
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]