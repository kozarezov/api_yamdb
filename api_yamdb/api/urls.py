from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api import views

app_name = 'api'

router = SimpleRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
]
