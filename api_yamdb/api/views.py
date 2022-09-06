from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from api import serializers
from api import permissions
from users.models import User


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


class UserToken(APIView):
    """Получение токена."""
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.data['username'])

        if default_token_generator.check_token(
            user, request.data['confirmation_code']
        ):
            token = AccessToken.for_user(user)
            return Response(
                {'token': str(token)}, status=status.HTTP_200_OK
            )
        return Response(
            {'Ошибка формирования токена'},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для добавления/изменения/удаления пользователей."""

    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = (permissions.IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
