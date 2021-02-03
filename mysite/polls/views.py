from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import json

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # pegamos os cinco ultimas questions publicadas
    output = ' '.join([q.question_text for q in latest_question_list])  # pega cada um dos titulos das questions
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"Você está olhando a questão {question_id}")


def results(request, question_id):
    response = f'Você está olhando para os resultados da questão {question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
