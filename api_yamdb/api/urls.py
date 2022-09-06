from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api import views

app_name = 'api'

router = SimpleRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', views.UserSignUp.as_view()),
    path('v1/auth/token/', views.UserToken.as_view()),
]
