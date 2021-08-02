from django.db import models


class Klasa(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
class Przedmiot(models.Model):
    name = models.CharField(max_length=128)
    klasa =models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Nauczyciel(models.Model):
    name = models.CharField(max_length=128)
    klasa = models.ManyToManyField(Klasa)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=128)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Ocena(models.Model):
    ndst = "1"
    ndstplus = "1+"
    dopminus = "2-"
    dop = "2"
    dopplus = "2+"
    dstminus = "3-"
    dst = "3"
    dstplus = "3+"
    dbminus = "4-"
    db = "4"
    dbplus = "4+"
    bdbminus = "5-"
    bdb = "5"
    bdbplus = "5+"
    celminus = "6-"
    cel = "6"
    mozliwe_oceny =[(ndst, "1"),
                    (ndstplus, "1+"),
                    (dopminus, "2-"),
                    (dop, "2"),
                    (dopplus, "2+"),
                    (dstminus, "3-"),
                    (dst, "3"),
                    (dstplus, "3+"),
                    (dbminus, "4-"),
                    (db, "4"),
                    (dbplus, "4+"),
                    (bdbminus, "5-"),
                    (bdb, "5"),
                    (bdbplus, "5+"),
                    (celminus, "6-"),
                    (cel, "6")]
    name = models.CharField(max_length=4,choices=mozliwe_oceny)
    pub_date = models.DateTimeField(auto_now_add=True)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

