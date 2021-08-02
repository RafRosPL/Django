from django.urls import path
from . import generic_views, views

app_name= "class_urls"

urlpatterns = [
    path('uczniowie/<int:pk>', generic_views.UczniowieDetailView.as_view(), name="uczniwie-detail-view")
]