from django.urls import path
from . import views

urlpatterns = [

    path('', views.listfiliére, name="filiére"),
    path('ajout_filiere/', views.ajouter_filiere, name='ajout_filiere'),
    path('modif_filiere/<str:pk>', views.modifier_filiere, name='modif_filiere'),
    path('_supprime_filiere/<str:pk>', views.supprimer_filiere, name='supprime_filiere'),
]
