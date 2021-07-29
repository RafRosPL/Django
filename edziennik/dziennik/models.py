from django.db import models


class Klasa(models.Model):
    name = models.CharField(max_length=128)

class Przedmiot(models.Model):
    name = models.CharField(max_length=128)
    klasa =models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True, blank=True)

class Nauczyciel(models.Model):
    name = models.CharField(max_length=128)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True, blank=True)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE, null=True, blank=True)

class Student(models.Model):
    name = models.CharField(max_length=128)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True, blank=True)

class Ocena(models.Model):
    name = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

