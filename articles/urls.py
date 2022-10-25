from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.create, name='create'),
    path('<str:slug>/', views.article_detail, name='detail'),
]
