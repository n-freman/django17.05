from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'cars/home.html', context)


def car(request, pk):
    # car = Post.objects.get(pk=pk) 
    car = get_object_or_404(Post, pk=pk)
    context = {
        'car': car
    }
    return render(request, 'cars/car.html', context)
