from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world!")  # resposta gerada quando essa função for chamada


def detail(request, question_id):
    return HttpResponse(f"Você está olhando a questão {question_id}")


def results(request, question_id):
    response = f'Você está olhando para os resultados da questão {question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
