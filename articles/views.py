from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleCreateForm


def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

def create(request):
    if request.method ==  'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = ArticleCreateForm()
    return render(request, 'articles/article_create.html', {'form':form})
