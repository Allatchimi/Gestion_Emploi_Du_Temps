from django.urls import path
from . import views

urlpatterns = [

    path('', views.listclasse, name="classe"),
    path('ajout_classe/', views.ajouter_classe, name='ajout_classe'),
    path('modif_classe/<str:pk>', views.modifier_classe, name='modif_classe'),
    path('_supprime_classe/<str:pk>', views.supprimer_classe, name='supprime_classe'),
]
