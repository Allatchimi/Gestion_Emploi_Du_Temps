from django.urls import path
from . import views

urlpatterns = [

    path('', views.listcours, name= "cours"),
    path('ajout_cours/', views.ajouter_cours, name='ajout_cours'),
    path('modif_cours/<str:pk>', views.modifier_cours, name='modif_cours'),
    path('_supprime_cours/<str:pk>', views.supprimer_cours, name='supprime_cours'),
]
