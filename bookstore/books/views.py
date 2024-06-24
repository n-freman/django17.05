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
from django.urls import reverse_lazy
from django.db.models import Subquery, OuterRef, Count, Exists
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from likes.models import Like
from .models import Book
from .permissions import OwnBookOrReadOnly
from .serializers import BookSerializer


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.user.is_authenticated:
            likes_subquery = Subquery(
                Like.objects.filter(
                    book=OuterRef('id'),
                    user=self.request.user
                )
            )
            queryset = queryset.annotate(is_liked=Exists(likes_subquery))
        return queryset


class MyBookListView(ListView):
    model = Book
    template_name = 'books/my_list.html'


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

    def get_queryset(self):
        likes_subquery = Subquery(
            Like.objects.filter(book=OuterRef('id')) \
                .values('id')
        )
        queryset = Book.objects.annotate(likes_count=Count(likes_subquery))
        if self.request.user.is_authenticated:
            likes_subquery = Subquery(
                Like.objects.filter(
                    book=OuterRef('id'),
                    user=self.request.user
                )
            )
            queryset = queryset.annotate(is_liked=Exists(likes_subquery))
        return queryset
