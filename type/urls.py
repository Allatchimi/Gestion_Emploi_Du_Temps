from django.urls import path
from . import views

urlpatterns = [

    path('', views.listtype, name="type"),
    path('ajout_type/', views.ajouter_type, name='ajout_type'),
    path('modif_type/<str:pk>', views.modifier_type, name='modif_type'),
    path('_supprime_type/<str:pk>', views.supprimer_type, name='supprime_type'),
]
