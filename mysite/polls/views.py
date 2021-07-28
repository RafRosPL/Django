from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll, Answer, Question


# def hello(request):
#     year = request.GET.get('year','other')
#     return HttpResponse(f'Hello, world! {year}')

def hello(request, s0):
    s1 = request.GET.get('s1',' ')
    return render(
        request, template_name="hello.html",
        context={'adjectives' : [s0, s1, 'beautiful','wonderful']}
    )
def dania(request, s0):
    s1 = request.GET.get('s1',' ')
    return render(
        request, template_name="my_template.html",
        context={'winners' : [s0, s1, 'Miłość','Dobro, a sędzia cwel']}
        )

def polls(request):
    return render(
        request,
        template_name="polls.html",
        context={"polls": Poll.objects.all()}
    )

def answers(request):
    return render(
        request,
        template_name="answers.html",
        context={"answers": Answer.objects.all()}
    )
def questions(request):
    return render(
        request,
        template_name="questions.html",
        context={"questions": Question.objects.all()}
    )
def index(request):
    return render(
        request,
        template_name="index.html")
