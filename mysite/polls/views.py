from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.http import Http404
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # pegamos a questão salva no bd
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # pegamos a opção selecionada
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1  # adicionamos um voto
        selected_choice.save()  # salvamos voto no banco de dados

        # é recomendável dar um retorno para quando usamos método post
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))  # redirecionamos o usuário
        # ele é enviado para a página polls/question_id/results/

