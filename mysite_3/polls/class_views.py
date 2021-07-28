from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404
from polls.models import Answer, Poll, Question
from django.views.generic import TemplateView , DetailView


class PollView(LoginRequiredMixin, View):
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
# class QuestionDetailView(View):
# 	def get(self,request,pk):
# 		return render(
# 			request,
# 			template_name="question.html",
# 			context={"question": Question.object.get(pk=pk)}
# 		)

class QuestionDetailView(View):
	def get(self,request,pk):
		obj = get_object_or_404(Question, pk=pk)
		return render(
			request,
			template_name="questions.html",
			context={"question":obj}
		)