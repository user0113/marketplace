"""
URL configurations for item app
"""

from django.urls import path

from . import views

app_name = 'dashboard'
"""
Establishes url pattern where path is item followed by a primary key integer
"""
urlpatterns = [
    path('', views.index, name='index')
]