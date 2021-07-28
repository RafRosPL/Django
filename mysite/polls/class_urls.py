from django.urls import path

from . import class_views

urlpatterns = [
    path('poll-class-view/', class_views.PollView.as_view(), name='poll-class-view')
]