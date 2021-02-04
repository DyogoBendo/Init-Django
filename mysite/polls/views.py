from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.template import loader
import json

# Create your views here.


class IndexView(generic.ListView):
    template_name = "polls/index.html"  # informamos qual template deve ser usado
    context_object_name = "latest_question_list"  # informamos qual o nome do objeto passado para o template

    def get_queryset(self):
        """
        :return: the last five published questions
        """
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    # ela espera pk como um parametro, por isso alteramos o nome
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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

