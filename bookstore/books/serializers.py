from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    likes_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.BooleanField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'image',
            'owner',
            'description',
            'title',
            'created_at',
            'likes_count',
            'is_liked'
        ]

    def save(self, **kwargs):
        kwargs['owner'] = self.fields['owner'].get_default()
        return super().save(**kwargs)
