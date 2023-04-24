from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Skills
from .serializers import SkillsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class SkillsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Skills.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=SkillsSerializer



class SkillGetByID(generics.GenericAPIView):
    def get(self,request,format=None):
        instances = Skills.objects.filter(user_id = self.request.user.id)
        serializer_response = SkillsSerializer(instances, many=True)
        return Response(data=serializer_response.data)