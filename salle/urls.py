from django.urls import path
from . import views

urlpatterns = [

    path('', views.listsalle, name="salle"),
    path('ajout_salle/', views.ajouter_salle, name='ajout_salle'),
    path('modif_salle/<str:pk>', views.modifier_salle, name='modif_salle'),
    path('_supprime_salle/<str:pk>', views.supprimer_salle, name='supprime_salle'),

]
