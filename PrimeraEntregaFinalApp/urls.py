from django.urls import path
from PrimeraEntregaFinalApp import views

urlpatterns = [
    
    path('', views.inicio, name="inicio"),
    path('base', views.base),
    path('socios', views.socios, name="socios"),
    path('deportes', views.deportes, name="deportes"),
    path('profesores', views.profesores, name="profesores"),
    path('crear_profesor/', views.crear_profesor, name="crear_profesor"),
    path('administracion', views.administracion, name="administracion"),
    path('crear_admin/', views.crear_administrador, name="crear_admin"),
    path('crear_socio/', views.crear_socio, name="crear_socio"),
    path('crear_deporte/', views.crear_deporte, name="crear_deporte"),
    path('buscar_apellido_socio', views.buscar_apellido_socio, name="buscar_apellido_socio"),
]