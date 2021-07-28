from django.views import View
from django.shortcuts import render
from polls.models import Answer, Poll, Question
from django.views.generic import ListView, TemplateView


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
    template_name = "form.html"
    form_class = QuestionModelForm
    success_url = reverse_lazy("polls_generic:question-list-view")
    def form_valid(self, form):
        result = super().form_valid(form)
        q = form.cleaned_data["question_text"]
        p = form.cleaned_data["pub_date"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=q, pub_date=p, poll=poll)
        return result

class PollFormView(FormView):
    template_name = "form.html"
    form_class = PollForm
    success_url = reverse_lazy("polls_generic:poll-list-view")
    def form_valid(self, form):
        result = super().form_valid(form)
        my_name = form.cleaned_data["name"]
        Poll.objects.create(name=my_name)
        return result

class AnswerFormView(FormView):
    template_name = "form.html"
    form_class = AnswerForm
    success_url = reverse_lazy("polls_generic:answer-list-view")
    def form_valid(self, form):
        result = super().form_valid(form)
        a = form.cleaned_data["answer_text"]
        d = form.cleaned_data["date_added"]
        q = form.cleaned_data["question"]
        Answer.objects.create(answer_text=a, date_added=d, question=q,)
        return result