from django.contrib import admin
from .models import Test, Question, Answer, UserAnswer


class TestAdmin(admin.ModelAdmin):
    fields = ('title', )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['test', 'type', 'text']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'correct']


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'question', 'answer']


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
