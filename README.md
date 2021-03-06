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
## Verificando se há algum problema no projeto
```
python manage.py check 
```
## Executando a migration
```
python manage.py migrate
```
### Shell do Python
```
python manage.py shell 
```
## Criando um usuário administrador
```
python manage.py createsuperuser
Username: admin
Email address: admin@example.comPassword: **********
Password (again): *********
Superuser created successfully. 
```

## Executando testes de polls
```
python manage.py test polls 
```

## Criando pacote
```
python setup.py sdist
```

## Instalando o pacote que criamos
```
python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
```