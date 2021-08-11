from django.shortcuts import render
from django.http import HttpResponse
from dziennik.models import Ocena, Przedmiot, Klasa, Student, Nauczyciel

def przedmioty(request):
    return render(
        request,
        template_name="przedmioty.html",
        context={"przedmioty": Przedmiot.objects.all()}
    )

def klasy(request):
    return render(
        request,
        template_name="klasa.html",
        context={"klasy": Klasa.objects.all()}
    )

def studenty(request):
    return render(
        request,
        template_name="student.html",
        context={"students": Student.objects.all()}
    )
def ocena(request):
    return render(
        request,
        template_name="ocena.html",
        context={"oceny": Student.objects.all()}
    )

def nauczyciele(request):
    return render(
        request,
        template_name="nauczyciele.html",
        context={"nauczyciele": Nauczyciel.objects.all()}
    )

def index(request):
    return render(
        request,
        template_name="index.html"
    )