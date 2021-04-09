# Generated by Django 3.2 on 2021-04-09 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_alter_rodada_data_rodada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_jogo', models.DateTimeField()),
                ('realizada', models.BooleanField(default=True)),
                ('gols_time1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('gols_time2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rodada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rodada', to='bets.rodada')),
                ('time1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='bets.time')),
                ('time2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='bets.time')),
            ],
            options={
                'ordering': ('rodada',),
                'index_together': {('id',)},
            },
        ),
    ]
