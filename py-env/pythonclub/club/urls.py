from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('getdetails/<int:id>', views.getdetails, name='getdetails'),
    path('newmeeting/', views.newmeeting, name='newmeeting'),
    path('newresource/', views.newresource, name='newresource'),
]