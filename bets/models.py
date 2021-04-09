from django.db import models

# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudo/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return self.nome



class Rodada(models.Model):
    nome_rodada = models.CharField(max_length=50)
    data_rodada = models.DateField(blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('id',)


    def __str__(self):
        return self.nome_rodada


class Jogo(models.Model):
    rodada = models.ForeignKey(Rodada,
                             on_delete=models.CASCADE,
                             related_name='rodada')
    time1 = models.ForeignKey(Time,
                              on_delete=models.CASCADE,
                              related_name='time1')
    time2 = models.ForeignKey(Time,
                              on_delete=models.CASCADE,
                              related_name='time2')

    data_jogo = models.DateTimeField(blank=False, null=False)
    realizada = models.BooleanField(default=True)
    gols_time1 = models.PositiveSmallIntegerField(blank=True, null=True)
    gols_time2 = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ('rodada',)


    def __str__(self):
        return f'{self.time1} X {self.time2}'