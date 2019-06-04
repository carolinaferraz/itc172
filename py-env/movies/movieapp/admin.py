from django.contrib import admin
from .models import Movie, Theater

# Register your models here.
admin.site.register(Theater)
admin.site.register(Movie)