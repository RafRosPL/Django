from django.contrib import admin
from movies.models import Actor, Country, Movie, Oscar

# Register your models here.

admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Movie)
admin.site.register(Oscar)