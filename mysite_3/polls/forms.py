from django.forms import CharField, DateTimeField, Form, ModelChoiceField, ModelForm
from polls.models import Poll, Question, Answer
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz
utc = pytz.UTC


def capitalized_validator(value):
	if value[0].islower():
		raise ValidationError('Start with capital letter!')

def question_mark_validator(value):
	if value[-1] != '?':
		raise ValidationError('End with queston mark [?]!')


class PastDateField(DateTimeField):

	def validate(self, value):
		super().validate(value)
		if value >= datetime.today().replace(tzinfo=utc):
			raise ValidationError('Only past dates allowed...')


class NameForm(Form):
	name = CharField(max_length=128)
	bith_date = DateTimeField()


class PollForm(Form):
	name = CharField(max_length=128)

	def clean_name(self):
		return self.cleaned_data['name'].upper()


class QuestionForm(Form):
	#question_text = CharField(max_length=128, validators=[capitalized_validator,
	#														question_mark_validator])
	question_text = CharField(max_length=128)
	#pub_date = PastDateField(label='Publication Date')
	pub_date=DateTimeField()
	poll = ModelChoiceField(queryset=Poll.objects.all())


	def clean_question_text(self):
		initial = self.cleaned_data['question_text']
		return initial.title()


	def clean(self):
		result = super().clean()
		if result['question_text'][0] == 'W' and result['pub_date'] > datetime.now(tz=utc):
			self.add_error('question_text','dont start with W')
			self.add_error('pub_date', 'to late, max 2000y')
			raise ValidationError('Nie W i nie pozniej niz 2000r')	

def upper_validator(value):
	if value.isupper():
		raise ValidationError('Turn off Caps-Lock!')


class AnswerForm(Form):
	answer_text = CharField(max_length=128, validators=[upper_validator])
	pub_date = DateTimeField()
	question = ModelChoiceField(queryset=Question.objects.all())


class QuestionModelForm(ModelForm):

	class Meta:
		model = Question
		fields = '__all__'


class AnswerModelForm(ModelForm):

	class Meta:
		model = Answer
		fields = '__all__'


class PollModelForm(ModelForm):

	class Meta:
		model = Poll
		fields = '__all__'

