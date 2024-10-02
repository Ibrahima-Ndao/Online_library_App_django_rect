from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions # type: ignore
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer

class UserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]  # Pour restreindre l'accès aux utilisateurs authentifiés
