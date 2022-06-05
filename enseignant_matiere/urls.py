from django.urls import path
from . import views

urlpatterns = [

    path('', views.listenseignant_matiere, name="enseignant_matiere"),
    path('ajout_enseignant_matiere/', views.ajouter_enseignant_matiere, name='ajout_enseignant_matiere'),
    path('modif_enseignant_matiere/<str:pk>', views.modifier_enseignant_matiere, name='modif_enseignant_matiere'),
    path('_supprime_enseignant_matiere/<str:pk>', views.supprimer_enseignant_matiere, name='supprime_enseignant_matiere'),
]
