from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'


class MyBookListView(ListView):
    model = Book
    template_name = 'books/my_list.html'
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user) \
            .all()


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


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/update.html'
    fields = ['title', 'image', 'description']

    def get_success_url(self) -> str:
        return reverse_lazy('home')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/delete.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')
