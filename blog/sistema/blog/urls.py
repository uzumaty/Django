from django.urls import path
from blog import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('otros/', views.otros, name='otros'),
    path('inicio/', views.inicio, name='inicio'),
    path('muro/', views.muro, name='muro'),
]
