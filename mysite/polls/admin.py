from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3  # são mostradas pelo menos 3 campos de Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {"fields" : ['pub_date'], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]  # adicionamos para que Choice possa ser editado em Question

    list_display = ("question_text", "pub_date", "was_published_recently")  # o que é mostrado na tela inicial
    list_filter = ["pub_date"]  # adicionamos a possibilidade de um filtro, a partir da data de publicação


admin.site.register(Question, QuestionAdmin)
