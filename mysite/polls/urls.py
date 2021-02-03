from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # mapeamos a url do index
    # adicionamos o caminho para acessar a view detail, passando o parametro question_id, que é um inteiro
    path('<int:question_id>/', views.detail, name="detail"),
    # caminho para results
    path('<int:question_id>/results/', views.results, name='results'),
    # caminho para votar
    path("<int:question_id>/vote/", views.vote, name="vote")
]
