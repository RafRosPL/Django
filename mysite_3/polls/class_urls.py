from django.urls import path
from . import class_views, views

app_name = 'class_urls'

urlpatterns = [
	path('poll-class-view/', class_views.PollView.as_view(), name="poll-class-view"),
	path('poll-class-form/', views.PollFormView.as_view(), name="poll-class-form"),
	path('answer-class-view/', class_views.AnswerView.as_view(), name="answer-class-view"),
	path('answer-class-form/', views.AnswerFormView.as_view(), name="answer-class-form"),
	path('question-class-view/', class_views.QuestionView.as_view(), name="quetion-class-view"),
	path('question-class-form/', views.QuestionFormView.as_view(), name="quetion-class-form"),
]