from django.db import models

# Create your models here.

class Time(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    escudo = models.ImageField(upload_to='escudo/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name