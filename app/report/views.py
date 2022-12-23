from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Report
from .serializers import ReportSerializer
from rest_framework import filters
from rest_framework import permissions
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ReportView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Report.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ReportSerializer




class AnnouncementView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        if(Report.objects.all().count()==0):
            item = ReportSerializer(data={'event_views':1,'announcement_views':1})
            item.is_valid(raise_exception=True)
            item.save()
            return Response()
        else:
            Report.objects.all().update(announcement_views=F('announcement_views')+1)
            return Response(status=status.HTTP_200_OK,data=[])


class EventView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        if(Report.objects.all().count()==0):
            item = ReportSerializer(data={'event_views':1,'announcement_views':1})
            item.is_valid(raise_exception=True)
            item.save()
            return Response()
        else:
            Report.objects.all().update(event_views=F('event_views')+1)
            return Response(status=status.HTTP_200_OK,data=[])