from django.urls import path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookUpdateView,
    BookDetailView,
)

urlpatterns = [
    path('<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('create', BookCreateView.as_view(), name='book-create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]
