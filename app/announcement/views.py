from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from datetime import date,timedelta
from decouple import config
class AnnouncementView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Announcement.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=AnnouncementSerializer

    def list(self,request):
        today = date.today() - timedelta(days=10)
        print(today)
        item = Announcement.objects.filter(date_created__gte=today)
        item = AnnouncementSerializer(item,many=True)
        return Response(data=item.data)




