from django.views.generic import TemplateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
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
    model = Student
    template_name = "student.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context["students"] = Student.objects.filter(klasa__id=kwargs['object'].id)
        return context

class UczniowieListView(ListView, LoginRequiredMixin):
    template_nama ="student.html"
    model =Student
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        print(kwargs['objects.id'])
        context["students"] = Student.objects.filter(klasa__id=kwargs['object'].id)
        return context

class Przedmiot2TemplateView(TemplateView):
    template_name = "przedmioty.html"
    model = Przedmiot
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        student = Student.objects.get(id=kwargs['pk'])
        klasa = student.klasa
        context["przedmioty"] = Przedmiot.objects.filter(klasa__id=klasa.id)
        return context

# class OcenaTemplateView(TemplateView):
#     template_name = "ocena.html"
#     model = Ocena


class PrzedmiotyDetailView(DetailView, LoginRequiredMixin):
    model = Przedmiot
    template_name ="przedmioty_detail_views.html"


class KlasaListView(ListView):
    template_name = "klasa.html"
    model = Klasa


class KlasaTemplateView(TemplateView):
    template_name = "klasa.html"
    extra_context = {'klasy': Klasa.objects.all()}

class KlasaCreateView(CreateView):
    model = Klasa
    template_name ="form_klasa.html"
    fields = "__all__"
    success_url = reverse_lazy('generic_urls:klasa-template-view')

class KlasaUpdateView(UpdateView):
	model = Klasa
	fields = ("name")
	template_name = "form_klasa.html"
	success_url = reverse_lazy("edziennik:klasa")

class KlasaDeleteView(DeleteView):
	model = Klasa
	template_name ="klasa_delete_form.html"
	success_url = reverse_lazy('generic_urls:klasa-list-view')

class PrzedmiotListView(ListView):
    template_name = "przedmioty.html"
    model = Przedmiot


class PrzedmiotTemplateView(TemplateView):
    template_name = "przedmioty.html"
    extra_context = {'przedmioty': Przedmiot.objects.all()}


class PrzedmiotCreateView(CreateView):
    model = Przedmiot
    template_name ="form_przedmiot.html"
    fields = "__all__"
    success_url = reverse_lazy('generic_urls:przedmiot-template-view')


class PrzedmiotUpdateView(UpdateView):
	model = Przedmiot
	fields = ("name")
	template_name = "form_przedmiot.html"
	success_url = reverse_lazy("edziennik:przedmiot")


class PrzedmiotDeleteView(DeleteView):
	model = Przedmiot
	template_name ="przedmiot_delete_form.html"
	success_url = reverse_lazy('generic_urls:przedmiot-list-view')

class NauczycielListView(ListView):
    template_name = "nauczyciele.html"
    model = Nauczyciel


class NauczycielTemplateView(TemplateView):
    template_name = "nauczyciele.html"
    extra_context = {'nauczyciele': Nauczyciel.objects.all()}


class NauczycielCreateView(CreateView):
    model = Nauczyciel
    template_name ="form_nauczyciel.html"
    fields = "__all__"
    success_url = reverse_lazy('generic_urls:nauczyciel-template-view')


class NauczycielUpdateView(UpdateView):
	model = Nauczyciel
	fields = ("name")
	template_name = "form_nauczyciel.html"
	success_url = reverse_lazy("edziennik:nauczyciel")


class NauczycielDeleteView(DeleteView):
	model = Nauczyciel
	template_name ="nauczyciel_delete_form.html"
	success_url = reverse_lazy('generic_urls:nauczyciel-list-view')


class StudentlListView(ListView):
    template_name = "student.html"
    model = Student


class StudentTemplateView(TemplateView):
    template_name = "student.html"
    extra_context = {'students': Student.objects.all()}


class StudentCreateView(CreateView):
    model = Student
    template_name ="form_student.html"
    fields = "__all__"
    success_url = reverse_lazy('generic_urls:student-template-view')


class StudentUpdateView(UpdateView):
	model = Student
	fields = ("name")
	template_name = "form_student.html"
	success_url = reverse_lazy("edziennik:student")


class StudentDeleteView(DeleteView):
	model = Student
	template_name ="student_delete_form.html"
	success_url = reverse_lazy('generic_urls:student-template-view')


