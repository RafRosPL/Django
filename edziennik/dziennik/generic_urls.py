from django.urls import path
from . import generic_views, views

app_name= "generic_urls"

urlpatterns = [
    path('uczniowie/<int:pk>', generic_views.UczniowieDetailView.as_view(), name="uczniowie-detail-view"),
    path('przedmioty/<int:pk>', generic_views.PrzedmiotyDetailView.as_view(), name="przedmioty-detail-view"),
]