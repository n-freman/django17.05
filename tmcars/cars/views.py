from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='login')
def my_cars(request):
    cars = Post.objects.filter(user=request.user)
    context = {
        'posts': cars
    }
    return render(request, 'cars/my_cars.html', context)
