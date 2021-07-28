from django.urls import path
from . import views

urlpatterns = [
	# path('hello/<int:year>',views.hello, name='hello')
	# path('hello/',views.hello, name='hello')
	path('hello/<s0>', views.hello, name='hello'),
	path('animals/<an>', views.animals, name='animals'),
	path('polls', views.polls, name='polls'),
	path('questions', views.questions, name='questions'),
	path('answers', views.answers, name='answers'),
	path('', views.index, name='index'),
	path('get-name-form', views.get_name, name='get_name'),
	path('poll-form', views.poll_form, name='poll_form'),
]