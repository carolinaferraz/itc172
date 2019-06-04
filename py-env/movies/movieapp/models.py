from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
        
class Movie (models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    url=models.URLField()
    rating=models.SmallIntegerField()
    description=models.CharField(max_length=255, blank=True)
    review=models.CharField(max_length=255, blank=True)
    name=models.ForeignKey(Theater, on_delete=models.DO_NOTHING) 
    

    def __str__(self):
        return self.title

    class Meta:
        db_table='movie'
        verbose_name_plural='movies'




