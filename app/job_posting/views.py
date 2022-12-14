from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import JobPosting
from .serializers import JobPostingSerializer
from rest_framework import filters
from rest_framework import permissions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db.models import F
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from django.template.loader import render_to_string, get_template
from decouple import config
class JobPostingView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=JobPosting.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=JobPostingSerializer



class NotifyGmail(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        item = User.objects.all()
        item = GetUserSerializer(item,many=True)
        emailList = []
        print(res.get('category'))
        for x in item.data:
            emailList.append(x['email'])
            print(x['email'])
        message = get_template('new_post.html').render({"password":""})
        if(res.get('category')=='announcement'):
            User.objects.all().update(notification_announcement=F('notification_announcement')+1)
        elif(res.get('category')=='events'):
            print('yesssss')
            User.objects.all().update(notification_event=F('notification_event')+1)
        elif(res.get('category')=='job'):
            User.objects.all().update(notification_job=F('notification_job')+1)
        msg = EmailMultiAlternatives('Notification', message,'mcuimpacts@gmail.com', emailList)
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK,data=[])


