from django.forms import CharField, DateTimeField, Form


class NameForm(Form):
	name = CharField(max_length=128)
	bith_date = DateTimeField()


class PollForm(Form):
	name = CharField(max_length=128)


class QuesttionModelForm(forms.ModelFrom):
	class Meta:
		model = Question
		fields = "__all__"
