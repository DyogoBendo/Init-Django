from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')  # mapeamos a url do index
]