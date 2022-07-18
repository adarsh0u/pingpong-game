from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.index,name='index'),
    path('scan/',views.scan,name='scans'),
    path('stop/',views.stop,name='stop'),
]