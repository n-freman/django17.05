from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'
