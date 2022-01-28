from django.urls import path, include
from django.shortcuts import render, redirect

from . import views

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('home', views.indexView, name='Home'),
    path('tarieven', views.tarievenView, name='Tarieven'),
    path('contact', views.contactView, name='Contact'),
    path('over-mittacutzz', views.overMittacutzzView, name='Over Mittacutzz'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('404', views.handler404, name="404"),
    path('500', views.handler500, name="500"),

]

