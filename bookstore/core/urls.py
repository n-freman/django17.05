"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from books.views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    MyBookListView,
    BooksAPIView,
    SingleBookAPIView
)
from users.views import RegisterView, email_verification

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('email-verification', email_verification, name='email-verification'),
    path('', BookListView.as_view(), name='home'),
    path('my-books', MyBookListView.as_view(), name='my-books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('api/books/', BooksAPIView.as_view(), name='books-api'),
    path('api/books/<int:pk>/', SingleBookAPIView.as_view(), name='single-book-api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
