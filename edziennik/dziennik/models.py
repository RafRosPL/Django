from django.db import models



class Przedmioty(models.Model):
    name = models.CharField(max_length=128)

