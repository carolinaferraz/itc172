from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getmovies/', views.getmovies, name='movies'),
    path('gettheaters/', views.gettheaters, name="theaters"),
    path('getdetails/<int:id>', views.getdetails, name="moviedetails"),
]
