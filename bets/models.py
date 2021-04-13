from django.db import models
from django.urls import reverse

class Time(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)
    imagem = models.ImageField(upload_to='escudos/%Y/%m/%d',
                              blank=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'time'
        verbose_name_plural = 'times'

    def __str__(self):
        return self.name



class Rodada(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    data_rodada = models.DateTimeField(blank=False, null=False)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'rodada'
        verbose_name_plural = 'rodadas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bets:jogo_list_by_rodada',
                       args=[self.slug])

class Jogo(models.Model):
    rodada = models.ForeignKey(Rodada,
                                 related_name='jogos',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)

    time1 = models.ForeignKey(Time,
                              related_name='time1',
                              on_delete=models.CASCADE)


    time2 = models.ForeignKey(Time,
                              related_name='time2',
                              on_delete=models.CASCADE)

    data_jogo = models.DateTimeField(blank=False, null=False)
    available = models.BooleanField(default=True)

    gols_time1 = models.PositiveSmallIntegerField(blank=True, null=True)
    gols_time2 = models.PositiveSmallIntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        index_together = (('id', 'slug'),) # indice com dois campos juntos, futura consulta por id e slug


    def get_absolute_url(self):
        return reverse('bets:jogo_detail',
                       args=[self.id, self.slug])