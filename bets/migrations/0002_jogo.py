# Generated by Django 3.2 on 2021-04-12 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('data_jogo', models.DateTimeField()),
                ('available', models.BooleanField(default=True)),
                ('gols_time1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('gols_time2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rodada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos', to='bets.rodada')),
                ('time1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='bets.time')),
                ('time2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='bets.time')),
            ],
            options={
                'ordering': ('id',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
