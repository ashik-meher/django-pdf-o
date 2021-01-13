from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views
from .views import GeneratePDF

urlpatterns = [
    path('', views.print, name="index.html"),


]
