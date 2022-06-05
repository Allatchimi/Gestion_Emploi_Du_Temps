from django.urls import path
from . import views

urlpatterns = [
    path('', views.listmatiére, name="matiére"),
    path('ajout_matiere/', views.ajouter_matiere, name='ajout_matiere'),
    path('modif_matiere/<str:pk>', views.modifier_matiere, name='modif_matiere'),
    path('_supprime_matiere/<str:pk>', views.supprimer_matiere, name='supprime_matiere'),
]
