from django.db import models

# Create your models here.


class Question(models.Model):  # criando a tabela
    # cada atributo representa um campo da tabela
    # cada atributo é uma instância da classe Field
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # esse parametro passado serve para dar um nome legivel para o campo
    # caso contrario, o nome legivel fica o nome do atributo


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # estabelecemos uma relação entre as tabelas Choice e Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
