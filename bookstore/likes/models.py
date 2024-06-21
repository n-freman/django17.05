from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'book'],
                name='unique_user_book'
            )
        ]
