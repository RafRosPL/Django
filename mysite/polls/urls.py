from django.urls import path

from . import views
from . import class_views

urlpatterns = [
    path('hello/<s0>/', views.hello, name='hello'),
    path('dania/<s0>/', views.dania, name='dania'),
    path("polls", views.polls, name="polls"),
    path("answers",views.answers, name="answers"),
    path("questions",views.questions, name="questions"),
    path("index",views.index, name="index"),
    path('poll-class-view/', class_views.PollView.as_view(), name="poll-class-view")

]




