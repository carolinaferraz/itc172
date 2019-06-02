from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie (models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    url=models.URLField()
    description=models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='movie'
        verbose_name_plural='movies'

class Theater(models.Model):    
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    comment=models.CharField(max_length=255, blank=True)
    url=models.URLField(blank=True)
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.name


    class Meta:
        db_table='theater'
        verbose_name_plural='theaters'


