from django.urls import path
from . import class_views, views

app_name= "class_urls"

urlpatterns = [
    path('uczniowie-detail-view/<int:pk>',class_views.UczniowieDetailView.as_view(),name="uczniwie-detail-view")
]