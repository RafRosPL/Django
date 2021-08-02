from django.urls import path
from . import views

app_name = 'dziennik'

urlpatterns = [
    path("uczniowie",views.studenty, name="uczniowie"),
]