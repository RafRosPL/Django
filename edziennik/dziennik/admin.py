from django.contrib import admin

from dziennik.models import  Ocena, Przedmiot, Klasa, Student, Nauczyciel

admin.site.register(Przedmiot)
admin.site.register(Ocena)
admin.site.register(Klasa)
admin.site.register(Student)
admin.site.register(Nauczyciel)