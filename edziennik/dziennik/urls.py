from django.urls import path
from . import views

app_name = 'edziennik'

urlpatterns= [
    path("przedmioty/", views.przedmioty, name="przedmioty"),
    path("klasy/", views.klasy, name="klasy"),
    path("nauczyciele/", views.nauczyciele, name="nauczyciele"),
    path('',views.index, name="index"),
]