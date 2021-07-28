from django.db import models

class Poll(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

# Lista dostepnych pol:
# https://www.webforefront.com/django/modeldatatypesandvalidation.html

class Question(models.Model):
	question_text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField(auto_now_add=True)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	answer_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', null=True, blank=True)

	def __str__(self):
		return self.answer_text
