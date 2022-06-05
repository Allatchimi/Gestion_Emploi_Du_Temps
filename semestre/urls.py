from django.urls import path
from . import views

urlpatterns = [

    path('', views.listsemestre, name="semestre"),
    path('ajout_semestre/', views.ajouter_semestre, name='ajout_semestre'),
    path('modif_semestre/<str:pk>', views.modifier_semestre, name='modif_semestre'),
    path('_supprime_semestre/<str:pk>', views.supprimer_semestre, name='supprime_semestre'),
]
