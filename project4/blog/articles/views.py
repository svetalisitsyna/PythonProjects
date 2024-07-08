from django.shortcuts import render
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")
