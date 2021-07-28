from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Answer, Poll, Question
from polls.forms import NameForm, PollForm, QuestionForm, AnswerForm
from django.urls import reverse
from polls.forms import AnswerModelForm, QuestionModelForm, PollModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
#def hello(request, year):
#	return HttpResponse(f'Hello World! {year}')

def hello(request, s0):
	s1 = request.GET.get('s1','')
	return render(
		request, 
		template_name='hello.html',
		context={'adjectives': [s0, s1, 'beautiful', 'wonderfull']})

def animals(request, an):
	return render(
		request, 
		template_name='my_template.html',
		context={'animals': an.split(',')})

def polls(request):
	return render(
		request,
		template_name='polls.html',
		context={'object_list': Poll.objects.all()}
		)

def questions(request):
	return render(
		request,
		template_name='questions.html',
		context={'object_list': Question.objects.all()}
	)

def answers(request):
	return render(
		request,
		template_name='answers.html',
		context={'object_list': Answer.objects.all()}
	)


def index(request):
	return render(
		request,
		template_name='index.html'
	)	
'''
def get_name(request):
	formularz = NameForm()
	if request.method == 'POST':
		formularz = NameForm(request.POST)
		if formularz.is_valid():
			return HttpResponse('It worked!')
		return HttpResponse('Incorrect data')
	return render(
		request,
		template_name='form.html',
		context={'form': formularz }
		)
'''
def get_name(request):
	formularz = NameForm(request.POST or None)
	if formularz.is_valid():
			return HttpResponse('It worked!')
	return render(
		request,
		template_name='form.html',
		context={'form': formularz }
		)

def poll_form(request):
	formularz = PollForm(request.POST or None)
	if formularz.is_valid():
			name = formularz.cleaned_data['name']
			Poll.objects.create(name=name)
			return render (
				request, 
				template_name='form_OK.html',
				context = {'form': 'Ankieta dodana.'}
				)
	return render(
		request,
		template_name='form.html',
		context={'form': formularz }
		)

def question_form(request):
	formularz = QuestionForm(request.POST or None)
	if formularz.is_valid():
			q = formularz.cleaned_data['question_text']
			pd = formularz.cleaned_data['pub_date']
			p = formularz.cleaned_data['poll']
			Question.objects.create(
				question_text = q,
				pub_date = pd,
				poll = p
				)
			return render (
				request, 
				template_name='form_OK.html',
				context = {'form': 'Pytanie dodane.'}
				)
	return render(
		request,
		template_name='form.html',
		context={'form': formularz }
		)

def answer_form(request):
	formularz = AnswerForm(request.POST or None)
	if formularz.is_valid():
			Answer.objects.create(
				answer_text = formularz.cleaned_data['answer_text'],
				pub_date = formularz.cleaned_data['pub_date'],
				question = formularz.cleaned_data['question']
				)
			return render (
				request, 
				template_name='form_OK.html',
				context = {'form': 'Odpowiedz dodana.'}
				)
	return render(
		request,
		template_name='form.html',
		context={'form': formularz }
		)

class PollFormView(View):
    def get(self, request):
        return render(
            request,
            template_name="form.html",
            context={"form": AnswerModelForm()}
        )
    def post(self, request):
        form = AnswerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("views:poll-class-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class AnswerFormView(View):
    def get(self, request):
        return render(
            request,
            template_name="form.html",
            context={"form": PollModelForm()}
        )
    def post(self, request):
        form = PollModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("views:poll-class-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
class QuestionFormView(View):
    def get(self, request):
        return render(
            request,
            template_name="form.html",
            context={"form": QuestionModelForm()}
        )
    def post(self, request):
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("views:question-class-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
