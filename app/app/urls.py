from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,GetUserView,Signup,ResetPassword,OTP,ApprovalOTP,ValidateUserAccount
from rest_framework import permissions
from work.views import WorkByUser
from job_posting.views import NotifyGmail
from skills.views import SkillGetByID
# from report.views import EventView,AnnouncementView,PostingView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/user/', GetUserView.as_view(), name='auth_data'),
    path('api/v1/approval-otp/', ApprovalOTP.as_view(), name='auth_data'),
    path('api/v1/reset-password/', ResetPassword.as_view(), name='auth_data'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/otp/', OTP.as_view(), name='token_refresh'),
    path('api/v1/notify/', NotifyGmail.as_view(), name='token_refresh'),
    path('api/v1/validate-user/', ValidateUserAccount.as_view(), name='token_refresh'),
    # path('api/v1/event-view/', EventView.as_view(), name='token_refresh'),
    path('api/v1/skill-get-by-id/', SkillGetByID.as_view(), name='token_refresh'),
    path('api/v1/work-user/', WorkByUser.as_view(), name='token_refresh'),
    # path('api/v1/announcement-view/', AnnouncementView.as_view(), name='token_refresh'),
    # path('api/v1/posting-view/', PostingView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/announcement/', include('announcement.urls')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/work/', include('work.urls')),
    path('api/v1/report/', include('report.urls')),
    path('api/v1/reset/', include('reset.urls')),
    path('api/v1/settings/', include('settings.urls')),
    path('api/v1/skills/', include('skills.urls')),
    path('api/v1/job_posting/', include('job_posting.urls')),
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]