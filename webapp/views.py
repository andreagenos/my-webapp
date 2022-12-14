from django.shortcuts import render

def article_list(request):
    return render(request, 'webapp/article_list.html', {})

# Create your views here.
