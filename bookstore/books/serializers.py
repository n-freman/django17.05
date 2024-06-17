from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Book
        fields = '__all__'

    def save(self, **kwargs):
        kwargs['owner'] = self.fields['owner'].get_default()
        return super().save(**kwargs)
