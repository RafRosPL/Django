from django.contrib import admin
from polls.models import Answer, Poll, Question

# Register your models here.

admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question)