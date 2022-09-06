from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', views.UserSignUp.as_view(), name='signup'),
    path('v1/auth/token/', views.UserToken.as_view(), name='token'),
]
