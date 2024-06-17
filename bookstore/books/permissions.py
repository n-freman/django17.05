import re

from rest_framework.permissions import BasePermission

from .models import Book


class OwnBookOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']: return True
        pattern = '\d+'
        match = re.search(pattern, request.path)
        if match is None: return True
        book_id = request.path[match.start():match.end()]
        book = Book.objects.filter(id=book_id)
        return not book.exists() or book.first().owner == request.user
