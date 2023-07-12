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

    def list(self,request):
        data = {}
        report_instance = Report.objects.all()
        serializer_response = ReportSerializer(report_instance, many=True)
        for x in serializer_response.data:
            user_serializer = User.objects.filter(id=x['user_id'])
            if(user_serializer.count() == 0):
                pass
            else:
                u_serializer_response = GetUserSerializer(user_serializer, many=True)
                x['users'] = u_serializer_response.data[0]

        return Response(data=serializer_response.data)




# class AnnouncementView(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny, )
#     def post(self,request):
#         if(Report.objects.all().count()==0):
#             item = ReportSerializer(data={'event_views':1,'announcement_views':1,'posting_views':1})
#             item.is_valid(raise_exception=True)
#             item.save()
#             return Response()
#         else:
#             Report.objects.all().update(announcement_views=F('announcement_views')+1)
#             return Response(status=status.HTTP_200_OK,data=[])


# class EventView(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny, )
#     def post(self,request):
#         if(Report.objects.all().count()==0):
#             item = ReportSerializer(data={'event_views':1,'announcement_views':1,'posting_views':1})
#             item.is_valid(raise_exception=True)
#             item.save()
#             return Response()
#         else:
#             Report.objects.all().update(event_views=F('event_views')+1)
#             return Response(status=status.HTTP_200_OK,data=[])

# class PostingView(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny, )
#     def post(self,request):
#         if(Report.objects.all().count()==0):
#             item = ReportSerializer(data={'event_views':1,'announcement_views':1,'posting_views':1})
#             item.is_valid(raise_exception=True)
#             item.save()
#             return Response()
#         else:
#             Report.objects.all().update(posting_views=F('posting_views')+1)
#             return Response(status=status.HTTP_200_OK,data=[])