from django.urls import path
from . import views

urlpatterns = [

    path('compte/inscription', views.inscriptionPage, name='inscription'),
    path('compte/acces', views.accesPage, name='acces'),
    path('compte/quitter', views.logoutUser, name='quitter'),

]