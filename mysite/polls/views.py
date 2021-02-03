from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
import json

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # pegamos os cinco ultimas questions publicadas
    context = {  # contexto mapeia nomes de variaveis para objeto python
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context)  # podemos simplificar dessa forma


def detail(request, question_id):
    return HttpResponse(f"Você está olhando a questão {question_id}")


def results(request, question_id):
    response = f'Você está olhando para os resultados da questão {question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
