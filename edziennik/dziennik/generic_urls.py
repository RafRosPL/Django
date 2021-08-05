from django.urls import path
from . import generic_views, views

app_name= "generic_urls"

urlpatterns = [
    path('uczniowie/<int:pk>', generic_views.UczniowieDetailView.as_view(), name="uczniowie-detail-view"),
    path('przedmioty/<int:pk>', generic_views.PrzedmiotyDetailView.as_view(), name="przedmioty-detail-view"),
    path('klasa-list-view/', generic_views.KlasaListView.as_view(), name="klasa-list-view"),
    path('klasa-template-view/', generic_views.KlasaTemplateView.as_view(), name="klasa-template-view"),
    path('klasa-create-view/', generic_views.KlasaCreateView.as_view(), name="klasa-create-view"),
    path('klasa-update-view/<int:pk>', generic_views.KlasaUpdateView.as_view(), name="klasa-update-view"),
    path('klasa-delete-view/<int:pk>', generic_views.KlasaDeleteView.as_view(), name="klasa-delete-view"),
    path('przedmiot-list-view/', generic_views.PrzedmiotListView.as_view(), name="przedmiot-list-view"),
    path('przedmiot-template-view/', generic_views.PrzedmiotTemplateView.as_view(), name="przedmiot-template-view"),
    path('przedmiot-create-view/', generic_views.PrzedmiotCreateView.as_view(), name="przedmiot-create-view"),
    path('przedmiot-update-view/<int:pk>', generic_views.PrzedmiotUpdateView.as_view(), name="przedmiot-update-view"),
    path('przedmiot-delete-view/<int:pk>', generic_views.PrzedmiotDeleteView.as_view(), name="przedmiot-delete-view"),
]