from django.urls import path
from . import generic_views, views

app_name= "generic_urls"

urlpatterns = [
    path('uczniowie/<int:pk>/', generic_views.UczniowieDetailView.as_view(), name="uczniowie-detail-view"),
    path('uczniowie/<int:pk>/', generic_views.UczniowieListView.as_view(), name="uczniowie-list-view"),
    path('przedmioty/<int:pk>/', generic_views.PrzedmiotyDetailView.as_view(), name="przedmioty-detail-view"),
    path('klasa-list-view/', generic_views.KlasaListView.as_view(), name="klasa-list-view"),
    path('klasa-template-view/', generic_views.KlasaTemplateView.as_view(), name="klasa-template-view"),
    path('klasa-create-view/', generic_views.KlasaCreateView.as_view(), name="klasa-create-view"),
    path('klasa-update-view/<int:pk>/', generic_views.KlasaUpdateView.as_view(), name="klasa-update-view"),
    path('klasa-delete-view/<int:pk>/', generic_views.KlasaDeleteView.as_view(), name="klasa-delete-view"),
    path('przedmiot-list-view/', generic_views.PrzedmiotListView.as_view(), name="przedmiot-list-view"),
    path('przedmiot2-template-view/<int:pk>/', generic_views.Przedmiot2TemplateView.as_view(), name="przedmiot2-template-view"),
    path('przedmiot-template-view/', generic_views.PrzedmiotTemplateView.as_view(), name="przedmiot-template-view"),
    path('przedmiot-create-view/', generic_views.PrzedmiotCreateView.as_view(), name="przedmiot-create-view"),
    path('przedmiot-update-view/<int:pk>/', generic_views.PrzedmiotUpdateView.as_view(), name="przedmiot-update-view"),
    path('przedmiot-delete-view/<int:pk>/', generic_views.PrzedmiotDeleteView.as_view(), name="przedmiot-delete-view"),
    path('nauczyciel-list-view/', generic_views.NauczycielListView.as_view(), name="nauczyciel-list-view"),
    path('nauczyciel-template-view/', generic_views.NauczycielTemplateView.as_view(), name="nauczyciel-template-view"),
    path('nauczyciel-create-view/', generic_views.NauczycielCreateView.as_view(), name="nauczyciel-create-view"),
    path('nauczyciel-update-view/<int:pk>/', generic_views.NauczycielUpdateView.as_view(), name="nauczyciel-update-view"),
    path('nauczyciel-delete-view/<int:pk>/', generic_views.NauczycielDeleteView.as_view(), name="nauczyciel-delete-view"),
    # path('student-list-view/', generic_views.StudentListView.as_view(), name="student-list-view"),
    path('student-template-view/', generic_views.StudentTemplateView.as_view(), name="student-template-view"),
    path('student-create-view/', generic_views.StudentCreateView.as_view(), name="student-create-view"),
    path('student-update-view/<int:pk>/', generic_views.StudentUpdateView.as_view(), name="student-update-view"),
    path('student-delete-view/<int:pk>/', generic_views.StudentDeleteView.as_view(), name="student-delete-view"),
    path('ocena-template-view/<int:uczen>/<int:pk>/', generic_views.OcenaTemplateView.as_view(), name="ocena-template-view"),
]