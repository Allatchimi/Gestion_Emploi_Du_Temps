from django.urls import path
from . import views

urlpatterns = [

    path('', views.listgroupe, name="groupe"),
    path('ajout_groupe/', views.ajouter_groupe, name='ajout_groupe'),
    path('modif_groupe/<str:pk>', views.modifier_groupe, name='modif_groupe'),
    path('_supprime_groupe/<str:pk>', views.supprimer_groupe, name='supprime_groupe'),
]
