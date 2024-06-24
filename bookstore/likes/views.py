import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from .models import Like
from .serializers import LikeSerializer


class LikesViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    '''
    Documentation for likes api
    <h3>I am using html here</h3>
    <img src="https://acdn.t-static.ru/static/documents/payment%20schema%20EACQ.jpg" />
    '''
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()

    def get_object(self):
        book_id = self.kwargs.get('pk')
        return get_object_or_404(
            Like,
            book=book_id,
            user=self.request.user
        )
