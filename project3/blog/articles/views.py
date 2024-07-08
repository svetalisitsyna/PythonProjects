from .models import Article
from django.shortcuts import render

def archive(request):
    posts = Article.objects.all()  # Получаем все объекты Article из базы данных
    return render(request, 'archive.html', {"posts": posts})
