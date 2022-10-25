from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
