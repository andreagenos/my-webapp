from django.shortcuts import render
from .models import Article
from django.utils import timezone

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'webapp/article_list.html', {'articles': articles})

# Create your views here.
