from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
                    ReviewViewSet, CommentViewSet, UserSignUp, UserToken)

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('categories', CategoryViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                   basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/('
                   r'?P<review_id>\d+)/comments', CommentViewSet,
                   basename='comments')

auth_urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='register'),
    path('token/', UserToken.as_view(), name='token')
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('auth/', include(auth_urlpatterns)),
]
