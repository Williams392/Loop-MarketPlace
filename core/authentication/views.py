# CREADA, no viene incluida:
from .serializers import LoginSerializer, UserSerializer  # 4
from .models import ProfileType, Profile

from datetime import datetime

from django.shortcuts import render

from django.contrib.auth import authenticate  # 5

from rest_framework.views import APIView  # 1
from rest_framework.response import Response  # 2
from rest_framework import status  # 3

from rest_framework.authtoken.models import Token  # 6
from rest_framework.authentication import TokenAuthentication  # 7
from rest_framework.permissions import IsAuthenticated  # 8


class LoginView(APIView):

    # Obteniendo el serializer de tipo USUARIO:
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        # Si no es NONE, Significa que el usuario existe y tiene credenciales válidas:
        if user is not None:
            user.last_login = datetime.now()
            user.save()

            # Para mostrar el token(contraseña), en la respuesta:
            token, _ = Token.objects.get_or_create(user=user)

            user_serializer = UserSerializer(user)
            user_serializer = dict(user_serializer.data)  # ConvertDiccionario.
            user_serializer['token'] = str(token.key)
            return Response(user_serializer, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "Las credenciales proporcionadas no son válidas. Por favor revise su información y vuelva a intentarlo."
                },
                status=status.HTTP_401_UNAUTHORIZED)


class SignUpView(APIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:  # Si :)

            user, profile_type_selected = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            user_serialized = UserSerializer(user)
            user_serialized = dict(user_serialized.data)
            user_serialized['token'] = str(token.key)
            user_serialized['profile_type'] = str(profile_type_selected)
            profile_type = ProfileType.objects.get(pk=profile_type_selected)
            profile = Profile.objects.create(
                user=user, profile_type=profile_type)
            return Response(user_serialized, status=status.HTTP_200_OK)

        except:  # No se logro guardar el objeto :(

            return Response(
                {
                    "error": "400 Bad Request",
                    "message": f"Email '{serializer.validated_data['email']}' is already registered"
                },
                status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response(
                {
                    "status": "200 OK",
                    "message": "Has terminado tu sesion satisfactoriamente"
                }
            )
        except Token.DoesNotExist:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "Token no asociado para el usuario"
                }, status=status.HTTP_401_UNAUTHORIZED
            )


"""
Apuntes:

1. APIView: Clase base para las vistas REST.
2. Response: Clase para devolver respuestas a los clientes.
3. status: Clase para devolver estados HTTP.

----------------------------------------------------------------
Cada Clase:

1.class LoginView:

_  Clase para el login de usuarios.
_ Se utiliza para autenticar a los usuarios utilizando las credenciales proporcionadas.
_ [urls.py] -> path('login/', LoginView.as_view(), name='login'),

2. class SignUpView:

_ Clase para el registro de usuarios.
_ Se utiliza para registrar nuevos usuarios en el sistema.
_ [urls.py] -> path('signup/', SignUpView.as_view(), name='signup'),

3. class LogoutView:

_ Se utiliza para manejar la funcionalidad de cierre de sesión en una API:
_ [urls.py] -> path('logout/', LogoutView.as_view(), name='logout'),

"""
