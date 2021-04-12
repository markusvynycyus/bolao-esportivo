from django.contrib import admin
from .models import Time, Rodada, Jogo

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}# campo onde o valor é definido automaticamente,usando valor de
                                              # de outro campo.

@admin.register(Rodada)
class RodadaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'data_rodada', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']# definir campos q podem ser editados na página de exibição  da lista do site adm.
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'rodada', 'data_jogo', 'time1', 'gols_time1', 'gols_time2', 'time2']
    list_filter = ['data_jogo', 'rodada', 'available', 'created', 'updated']
    list_editable = ['rodada']
    prepopulated_fields = {'slug': ('rodada',)}
