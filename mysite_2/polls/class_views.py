from django.views import View
from django.shortcuts import render
from polls.models import Answer, Poll, Question
from django.views.generic import TemplateView


class PollView(View):
	def get(self, request):
		return render(
			request,
			template_name='polls.html',
			context={'object_list': Poll.objects.all()}
			)


class AnswerView(View):
	def get(self, request):
		return render(
			request,
			template_name='answers.html',
			context={'object_list': Answer.objects.all()}
			)


class QuestionView(View):
	def get(self, request):
		return render(
			request,
			template_name='questions.html',
			context={'object_list': Question.objects.all()}
			)		