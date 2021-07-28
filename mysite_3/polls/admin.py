from django.contrib import admin
from django.contrib.admin import ModelAdmin
from polls.models import Answer, Poll, Question

# Register your models here.

admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question)


class Question(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'question_text', 'pub_year')
    list_display_links = ('id', 'question_text')
    list_per_page = 20
    list_filrer = ('pub_date',)
    search_fields = ("gquestion_text",)
    actions = ('cleanup_text',)

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(question_text="")
