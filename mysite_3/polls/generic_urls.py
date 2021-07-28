from django.urls import path
from . import generic_views

app_name = 'generic_urls'

urlpatterns = [
	path('poll-templates-view/', generic_views.PollTemplateView.as_view(), name="poll-templates-view"),
	path('poll-list-view/', generic_views.PollListView.as_view(), name="poll-list-view"),
	path('answer-templates-view/', generic_views.AnswerTemplateView.as_view(), name="answer-templates-view"),
	path('answer-list-view/', generic_views.AnswerListView.as_view(), name="answer-list-view"),
	path('question-templates-view/', generic_views.QuestionTemplateView.as_view(), name="question-templates-view"),
	path('question-create-view/', generic_views.QuestionCreateView.as_view(), name="question-create-view"),
	path('question-list-view/', generic_views.QuestionListView.as_view(), name="question-list-view"),
	path('question-generic-form/', generic_views.QuestionFormView.as_view(), name='question-generic-form'),
	path('answer-generic-form/', generic_views.AnswerFormView.as_view(), name='answer-generic-form'),
	path('poll-generic-form/', generic_views.PollFormView.as_view(), name='poll-generic-form'),
	path('question-delete-view/<int:pk>', generic_views.QuestionDeleteView.as_view(), name='question-delete-view'),
	path('answer-delete-view/<int:pk>', generic_views.AnswerDeleteView.as_view(), name='answer-delete-view'),
	path('poll-delete-view/<int:pk>', generic_views.PollDeleteView.as_view(), name='poll-delete-view'),
	path("question-detail-view/<int:pk>",generic_views.QuestionDetailView.as_view(), name="question-detail-view"),
	path("question-update-view/<int:pk>",generic_views.QuestionUpdateView.as_view(), name='question-update-view'),

]