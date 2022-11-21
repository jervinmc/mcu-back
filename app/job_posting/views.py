from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import JobPosting
from .serializers import JobPostingSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class JobPostingView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=JobPosting.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=JobPostingSerializer


