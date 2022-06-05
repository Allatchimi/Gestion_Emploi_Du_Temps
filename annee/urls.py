from django.urls import path
from . import views

urlpatterns = [

    path('', views.listannee, name='ann'),
    path('ajout_annee/', views.ajouter_annee, name='ajout_annee'),
    path('modif_annee/<str:pk>', views.modifier_annee, name='modif_annee'),
    path('_supprime_annee/<str:pk>', views.supprimer_annee, name='supprime_annee'),
]
