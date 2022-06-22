from django.contrib.auth import authenticate, get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, UpdateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token

from .serializers import *

CustomUser = get_user_model()


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    User authorization
    need to send json to the body like:

    {
      "email": "example@example.com",
      "password": "123456"
    }
    """

    login_serializer = UserLoginSerializer(data=request.data)

    if not login_serializer.is_valid():
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NoQa

    user = authenticate(
        username=login_serializer.data['email'],
        password=login_serializer.data['password']
    )

    if user and user.is_active is False:
        return Response({'detail': 'User is not active'},
                        status=status.HTTP_403_FORBIDDEN)

    if not user:
        return Response({'detail': 'Incorrect account login information'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data,
        'token': token.key
    }, status=status.HTTP_200_OK)


class Registration(generics.CreateAPIView):
    """Registration User"""
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()


class Logout(APIView):
    """
    Logout User
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(status=status.HTTP_200_OK)


class UserList(generics.ListAPIView):
    """List all users"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
    pagination_class = None


class GroupsViewSet(ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    pagination_class = None


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = None


class LastWinnersViewSet(ListAPIView):
    queryset = LastWinners.objects.all()
    serializer_class = LastWinnersSerializer
    pagination_class = None


class ArchiveViewSet(ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    pagination_class = None


class CommandCreateViewSet(generics.CreateAPIView):
    serializer_class = CommandCreateSerializer
    queryset = CommandParticipatingNow.objects.all()


class CommandViewSet(ListAPIView):
    serializer_class = CommandCreateSerializer
    queryset = CommandParticipatingNow.objects.all()
    pagination_class = None


class DuelViewSet(ListAPIView):
    serializer_class = DuelSerializer
    queryset = DuelParticipatingNow.objects.all()
    pagination_class = None


class AddDuelViewSet(generics.CreateAPIView):
    serializer_class = DuelSerializer
    queryset = DuelParticipatingNow.objects.all()


class UpdateDuelViewSet(UpdateAPIView):
    serializer_class = DuelSerializer
    queryset = DuelParticipatingNow.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "acceptDuel update true"})

        else:
            return Response({"message": "acceptDuel update false"})


class DeleteDuelViewSet(generics.DestroyAPIView):
    serializer_class = DuelSerializer
    queryset = DuelParticipatingNow.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "delete false"})

