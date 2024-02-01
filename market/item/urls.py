"""
URL configurations for item app
"""

from django.urls import path

from . import views

app_name = 'item'
"""
Establishes url pattern where path is item followed by a primary key integer
"""
urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail')
    
]