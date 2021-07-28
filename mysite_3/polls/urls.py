from django.urls import path
from . import views


app_name = 'polls'

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
	path('question-form', views.question_form, name='question_form'),
	path('answer-form', views.answer_form, name='answer_form'),
]
