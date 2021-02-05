from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3  # são mostradas pelo menos 3 campos de Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {"fields" : ['pub_date'], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]  # adicionamos para que Choice possa ser editado em Question


admin.site.register(Question, QuestionAdmin)
