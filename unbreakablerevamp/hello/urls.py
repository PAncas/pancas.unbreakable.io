from django.urls import path

#from current directory import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home")
]