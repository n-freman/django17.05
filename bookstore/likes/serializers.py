from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Like.objects.all(),
                fields=['user', 'book']
            )
        ]

    def save(self, **kwargs):
        kwargs['user'] = self.fields['user'].get_default()
        return super().save(**kwargs)
