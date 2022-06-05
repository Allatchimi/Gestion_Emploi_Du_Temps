from django.urls import path
from . import views

urlpatterns = [

    path('', views.listenseignant, name="enseignant"),
    path('ajout_enseignant/', views.ajouter_enseignant, name='ajout_enseignant'),
    path('modif_enseignant/<str:pk>', views.modifier_enseignant, name='modif_enseignant'),
    path('_supprime_enseignant/<str:pk>', views.supprimer_enseignant, name='supprime_enseignant'),
]
