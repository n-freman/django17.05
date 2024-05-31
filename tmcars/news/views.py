from django.shortcuts import render, get_object_or_404

from .models import News


def home(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/home.html', context)


def news_page(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {
        'news': news
    }
    return render(request, 'news/item.html', context)
