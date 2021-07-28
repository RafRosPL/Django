from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import render
from polls.models import Answer, Poll, Question
from polls.forms import QuestionForm, AnswerForm, PollForm, QuestionModelForm, PollModelForm, AnswerModelForm
from django.views.generic import (
	CreateView,
	ListView,
	TemplateView,
	FormView,
	UpdateView,
	DetailView,
	DeleteView)
from django.contrib.auth.mixins import UserPassesTestMixin


class PollTemplateView(TemplateView):
	template_name = 'polls.html'
	extra_context = {'object_list': Poll.objects.all()}


class PollListView(ListView):
	template_name = 'polls.html'
	model = Poll


class AnswerTemplateView(TemplateView):
	template_name = 'answers.html'
	extra_context = {'object_list': Answer.objects.all()}


class AnswerListView(ListView):
	template_name = 'answers.html'
	model = Answer


class QuestionTemplateView(TemplateView):
	template_name = 'questions.html'
	extra_context = {'object_list': Question.objects.all()}


class QuestionListView(ListView):
	template_name = 'questions.html'
	model = Question


class QuestionFormView(FormView):
	template_name = 'form.html'
	#form_class = QuestionForm
	form_class = QuestionModelForm
	success_url = reverse_lazy('generic_urls:question-generic-form')

	def form_valid(self, form):
		result = super().form_valid(form)
		q = form.cleaned_data["question_text"]
		#p = form.cleaned_data["pub_date"]
		poll = form.cleaned_data["poll"]
		#Question.objects.create(question_text=q, pub_date=p, poll=poll)
		Question.objects.create(question_text=q, poll=poll)
		return result

class AnswerFormView(FormView):
	template_name = 'form.html'
	#form_class = AnswerModelForm
	form_class = AnswerModelForm
	success_url = reverse_lazy('generic_urls:answer-generic-form')

	def form_valid(self, form):
		result = super().form_valid(form)
		a = form.cleaned_data["answer_text"]
		#p = form.cleaned_data["pub_date"]
		question = form.cleaned_data["question"]
		#Answer.objects.create(answer_text=a, pub_date=p, question=question)
		Answer.objects.create(answer_text=a,question=question)
		return result


class PollFormView(FormView):
	template_name = 'form.html'
	#form_class = PollForm
	form_class = PollModelForm
	success_url = reverse_lazy('generic_urls:poll-generic-form')

	def form_valid(self, form):
		result = super().form_valid(form)
		n = form.cleaned_data["name"]
		Poll.objects.create(name=n)
		return result

class QuestionCreateView(CreateView):
	model = Question
	template_name ='form.html'
	fields = '__all__'
	succes_url = reverse_lazy('generic_urls:question-list-view')
class QuestionDetailView(DetailView):
 	model = Question
class QuestionUpdateView(UpdateView):
	model = Question
	fields = ("question_text")
	template_name = "form.html"
	success_url = reverse_lazy("polls:questions")
class QuestionDeleteView(DeleteView):
	model = Question
	template_name ="delete_form.html"
	success_url = reverse_lazy('generic_urls:question-list-view')
class AnswerDeleteView(DeleteView):
	model = Answer
	template_name ="delete_form.html"
	success_url = reverse_lazy('generic_urls:answer-list-view')

class UserIsLoggedInMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated

class PollDeleteView(UserIsLoggedInMixin, DeleteView):
	model = Poll
	template_name ="delete_form.html"
	success_url = reverse_lazy('generic_urls:poll-list-view')

