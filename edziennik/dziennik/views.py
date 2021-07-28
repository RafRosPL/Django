from django.shortcuts import render
from django.http import HttpResponse
from dziennik.models import Przedmioty

def dziennik(request):
    return render(
        request,
        template_name="przedmioty.html",
        context={"przedmioty": Przedmioty.objects.all()}
    )
