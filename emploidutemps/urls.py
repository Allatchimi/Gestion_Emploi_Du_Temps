"""emploidutemps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashbord.urls')),
    path('cours', include('cours.urls')),
    path('enseignant', include('enseignant.urls')),
    path('filiére', include('filiére.urls')),
    path('matiére', include('matiére.urls')),
    path('salle', include('salle.urls')),
    path('ann', include('annee.urls')),
    path('groupe', include('groupe.urls')),
    path('classe', include('classe.urls')),
    path('semestre', include('semestre.urls')),
    path('type', include('type.urls')),
    path('enseignant_matiere', include('enseignant_matiere.urls')),
    path('matiere_semestre', include('matiere_semestre.urls')),
    path('', include('compte.urls')),

]
