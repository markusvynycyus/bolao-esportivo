from django.contrib import admin

from .models import Time, Rodada, Jogo

admin.site.register(Time)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['id','rodada','data_jogo','time1','gols_time1','gols_time2','time2']
    list_filter = ['data_jogo','rodada']

@admin.register(Rodada)
class RodadaAdmin(admin.ModelAdmin):
    list_display = ['id','nome_rodada','data_rodada']
    list_filter = ['nome_rodada', 'data_rodada']



