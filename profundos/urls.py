from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'knn/',
        view= views.KNNView.as_view(),
        name='knn',
    ),
    path(
        'perceptronNAND/',
        view= views.PerceptronNAND.as_view(),
        name='perceptronNAND',
    ),
    
    path(
        'bayesTexto/',
        view= views.BayesTexto.as_view(),
        name='bayesTexto',
    ),

    path(
        'multiClase/',
        view= views.MultiClase.as_view(),
        name='multiClase',
    ),

    path(
        'biClase/',
        view= views.BiClase.as_view(),
        name='biClase',
    ),
]