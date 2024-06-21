from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from books.views import BooksViewSet
from likes.views import LikesViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, 'book')
router.register('likes', LikesViewSet, 'likes')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
