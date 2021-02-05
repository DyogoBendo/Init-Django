from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):  # criando a tabela
    # cada atributo representa um campo da tabela
    # cada atributo é uma instância da classe Field
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # esse parametro passado serve para dar um nome legivel para o campo
    # caso contrario, o nome legivel fica o nome do atributo

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = "pub_date"  # parametro usado para ordenar
    was_published_recently.boolean = True  # é considerada uma booleans, então passa a mostrar de forma mais clara isso
    was_published_recently.shor_description = "Published recently!"  # mensagem que é mostrada


datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # estabelecemos uma relação entre as tabelas Choice e Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
