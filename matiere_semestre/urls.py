from django.urls import path
from . import views

urlpatterns = [

    path('', views.listmatiere_semestre, name="matiere_semestre"),
    path('ajout_matiere_semestre/', views.ajouter_matiere_semestre, name='ajout_matiere_semestre'),
    path('modif_matiere_semestre/<str:pk>', views.modifier_matiere_semestre, name='modif_matiere_semestre'),
    path('_supprime_matiere_semestre/<str:pk>', views.supprimer_matiere_semestre, name='supprime_matiere_semestre'),
]
