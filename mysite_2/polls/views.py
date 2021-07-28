from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Answer, Poll, Question
from polls.forms import NameForm, PollForm

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
		context={'questions': Question.objects.all()}
	)

def answers(request):
	return render(
		request,
		template_name='answers.html',
		context={'answers': Answer.objects.all()}
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

