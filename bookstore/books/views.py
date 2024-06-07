from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/create.html'
    fields = ['title', 'image', 'description']

    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return http.HttpResponseRedirect(self.get_success_url())
