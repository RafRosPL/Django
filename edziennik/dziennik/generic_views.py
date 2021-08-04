from django.views.generic import TemplateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404
from dziennik.models import Ocena, Przedmiot, Klasa, Student, Nauczyciel
from django.views.generic import (
	CreateView,
	ListView,
	TemplateView,
	FormView,
	UpdateView,
	DetailView,
	DeleteView)

class UczniowieDetailView(DetailView, LoginRequiredMixin):
    # def get(self, request, pk):
    #     obj = get_object_or_404(Student, pk=pk)
    #     return render(
    #         request,
    #         template_name="student.html",
    #         context={"student":obj}
    #     )
    model = Student
    template_name="student.html"

class PrzedmiotyDetailView(DetailView, LoginRequiredMixin):
    model = Przedmiot
    template_name="przedmioty_detail_views.html"

class KlasaListView(ListView):
    template_name = "klasa.html"
    model = Klasa


