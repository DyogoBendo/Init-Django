from django.urls import path
from . import views

app_name = "polls"  # definindo o namespace da aplicação e de suas rotas
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # mapeamos a url do index
    # adicionamos o caminho para acessar a view detail, passando o parametro question_id, que é um inteiro
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # caminho para results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # caminho para votar
    path("<int:question_id>/vote/", views.vote, name="vote")
]
