from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from user_account.accounts.models import CustomUser
from user_account.user_account.serializer import UserCreateSerializer


class Registration(generics.CreateAPIView):
    """Registration User"""
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
