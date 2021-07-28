from django.db import models

# Create your models here.
'''
a) Actor - pola: name, last_name, age, gender
b) Movie - pola: title, genre, year
c) Country - pola: name, iso_code
d) Oscar - pola: category, year

a) Aktor/ka mogą grać w kilku ﬁlmach
b) Film może mieć kilka oscarów, aktor/aktorka również - nie mogą się one jednak powtarzać
c) Kilka ﬁlmów może pochodzić z tego samego kraju
'''

class Actor(models.Model):
	name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	age = models.PositiveSmallIntegerField()
	gender = models.CharField(max_length=1, choices=[('F','Female'), ('M','Male')])

	def __str__(self):
		return f'{self.id}. {self.name} {self.last_name} - {self.age}yrs - {self.gender}'	

class Country(models.Model):
	name = models.CharField(max_length=128)
	iso_code = models.CharField(max_length=3)
	
	def __str__(self):
		return f'{self.iso_code}-{self.name}'


class Movie(models.Model):
	title = models.CharField(max_length=256)
	genre = models.CharField(max_length=64)
	year = models.PositiveSmallIntegerField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)
	
	def __str__(self):
		return f'{self.title}'


class Oscar(models.Model):
	category = models.CharField(max_length=128)
	year = models.PositiveSmallIntegerField()
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='oscars', null=True, blank=True)
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='oscars', null=True, blank=True)
	
	def __str__(self):
		return f'{self.year}-{self.category}'			


'''class Question(models.Model):
	question_text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField(auto_now_add=True)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)'''