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
    # def get(self, request, pk):
    #     obj = get_object_or_404(Student, pk=pk)
    #     return render(
    #         request,
    #         template_name="student.html",
    #         context={"student":obj}
    #     )
    model = Student
    template_name = "student.html"

class UczniowieListView(ListView, LoginRequiredMixin):
    template_nama ="student.html"
    model =Student
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Klasa.objects.all()
        return context


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

