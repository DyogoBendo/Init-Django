# Iniciando com Django
Esse é um projeto desenvolvido a partir de um [tutorial](https://docs.djangoproject.com/pt-br/3.1/intro/tutorial01/)

## Instalação
```
python -m pip install Django
```
## Iniciando projeto
```
django-admin startproject mysite
```
## Iniciando servidor
```
python manage.py runserver
```
## Criando aplicação
```
python manage.py startapp polls
```
## Atualizando tabelas do Banco de dados
```
python manage.py migrate
```
## Realizando migrations da aplicação polls
```
python manage.py makemigrations polls 
```
## Visualizando os comandos SQL da migration 001, da aplicação polls
```
 python manage.py sqlmigrate polls 0001 
```
