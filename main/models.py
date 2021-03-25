from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=1000)
    description = models.TextField(max_length=6000)
    release_date = models.DateField()
    averageRating = models.FloatField()

    def __unicode__(self):
        return self.name


    def __str__(self):
        return self.name