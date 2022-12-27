from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Work
from .serializers import WorkSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class WorkView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Work.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=WorkSerializer


class WorkByUser(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        item = Work.objects.filter(user_id = self.request.user.id)
        item = WorkSerializer(item,many=True)
        return Response(status=status.HTTP_200_OK,data=item.data)

