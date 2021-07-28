from django.urls import path
from . import class_views

urlpatterns = [
	path('poll-class-view/', class_views.PollView.as_view(), name="poll-class-view"),
	path('answer-class-view/', class_views.AnswerView.as_view(), name="answer-class-view"),
	path('question-class-view/', class_views.QuestionView.as_view(), name="quetion-class-view"),
]