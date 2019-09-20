from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.fibonacci,name='fibonacci'),
    path('add',views.add,name='add')
]