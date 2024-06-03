from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm
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


@login_required
def add_car(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Successfully created post'
            )
            return redirect('my-cars')
    context = {
        'form': form,
    }
    return render(request, 'cars/add.html', context)


@login_required
def edit_car(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only edit your own cars!'
        )
        return redirect('my-cars')
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(
            data=request.POST,
            files=request.FILES,
            instance=post
        )
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Successfully edited car'
            )
            return redirect('my-cars')
    context = {
        'form': form
    }
    return render(request, 'cars/edit.html', context)


@login_required
def delete_car(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own cars!'
        )
        return redirect('my-cars')
    post.delete()
    messages.add_message(
        request,
        messages.INFO,
        'Deleted car...'
    )
    return redirect('my-cars')
