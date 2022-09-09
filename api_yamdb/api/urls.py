from api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('users', views.UserViewSet, basename='users')
v1_router.register('categories', views.CategoryViewSet)
v1_router.register('genres', views.GenreViewSet)
v1_router.register('titles', views.TitleViewSet)
v1_router.register(r'titles/(?P<title_id>\d+)/reviews', views.ReviewViewSet,
                   basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/('
                   r'?P<review_id>\d+)/comments', views.CommentViewSet,
                   basename='comments')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', views.UserSignUp.as_view(), name='signup'),
    path('v1/auth/token/', views.UserToken.as_view(), name='token'),
]
