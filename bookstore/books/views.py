from django import http
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .permissions import OwnBookOrReadOnly
from .serializers import BookSerializer


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


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, OwnBookOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
