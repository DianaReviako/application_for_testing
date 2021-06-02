from django.contrib import admin
from .models import Test, Question, Answer, UserAnswer


class TestAdmin(admin.ModelAdmin):
    fields = ['title']


class QuestionAdmin(admin.ModelAdmin):
    fields = ('test', 'type', 'text')


class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'text', 'correct')


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer)
