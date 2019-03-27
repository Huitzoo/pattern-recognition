from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'metricas/',
        view=views.metricas,
        name='metricas',
    ),
     
    path(
        'euclideano/',
        view=views.euclideano,
        name='euclideano',
    ),
    path(
        'estadistico/',
        view=views.estadistico,
        name='estadistico',
    ),
    path(
        'bayesSimple/',
        view=views.bayesSimple,
        name='bayesSimple',
    ),
    
]