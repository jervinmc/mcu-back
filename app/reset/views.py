from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Reset
from .serializers import ResetSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ResetView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Reset.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=ResetSerializer


