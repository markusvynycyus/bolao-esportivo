from django.urls import path
from . import views

app_name = 'aposta'

urlpatterns = [
    path('', views.aposta_detail, name='aposta_detail'),
    path('add/<int:jogo_id>/', views.aposta_add, name='aposta_add'),
    path('remove/<int:jogo_id>/', views.aposta_remove, name='aposta_remove'),
]