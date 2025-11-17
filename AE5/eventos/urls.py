from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('nuevo/', views.registrar_evento, name='registrar_evento'),
]
