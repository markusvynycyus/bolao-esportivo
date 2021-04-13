from django.urls import path
from .import views

app_nome = 'bets'

urlpatterns = [
    path('', views.jogo_list, name='jogo_list'),
    path('<slug:rodada_slug>/', views.jogo_list, name='jogo_list_by_rodada'),
    path('<int:id>/<slug:slug>/', views.jogo_detail, name='jogo_detail'),
]

