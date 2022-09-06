from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from api import serializers


class UserSignUp(APIView):
    """Регистрация пользователя."""

    permission_classes = (AllowAny,)

    def send_confirmation_code(self, user):
        """Отправка кода на email."""
        token = default_token_generator.make_token(user)

        send_mail(
            subject='Confirmation code',
            message=f'Ваш код: {token}',
            from_email='robot@yamdb.ru',
            recipient_list=[user.email]
        )

    def post(self, request):
        serializer = serializers.UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.send_confirmation_code(user)
        return Response(serializer.data, status.HTTP_200_OK)
