from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.utils import timezone
from .managers import CustomUserManager
import uuid

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    MALE='Male'
    USERNAME_FIELD = 'email'
    FEMALE='Female'
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site.'),blank=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    ),blank=True)
    date_joined = models.DateTimeField(
        _('date_joined'), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True,blank=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    gender=models.CharField(_('gender'),max_length=255,blank=True,null=True)
    student_number=models.CharField(_('student_number'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    mobile_number=models.CharField(_('mobile_number'),max_length=255,blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    course=models.CharField(_('course'),max_length=255,blank=True,null=True)
    province=models.CharField(_('province'),max_length=255,blank=True,null=True)
    city=models.CharField(_('city'),max_length=255,blank=True,null=True)
    password=models.CharField(_('password'),max_length=255,blank=True,null=True)
    birthdate=models.CharField(_('birthdate'),max_length=255,blank=True,null=True)
    barangay=models.CharField(_('barangay'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True,null=True)
    religion=models.CharField(_('religion'),max_length=255,blank=True,null=True)
    age=models.CharField(_('age'),max_length=255,blank=True,null=True)
    civil_status=models.CharField(_('civil_status'),max_length=255,blank=True,null=True)
    last_attended=models.CharField(_('last_attended'),max_length=255,blank=True,null=True)
    work_status=models.CharField(_('work_status'),max_length=255,blank=True,null=True)
    country_code=models.CharField(_('country_code'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,unique=True,null=True)
    is_active=models.BooleanField(_('is_active'),default=True)
    notification_announcement = models.IntegerField(_('notification_announcement'),default=0.0)
    notification_job = models.IntegerField(_('notification_announcement'),default=0.0)
    notification_event = models.IntegerField(_('notification_event'),default=0.0)
    no_people = models.IntegerField(_('no_people'),default=0.0)
    account_type=models.CharField(_('account_type'),max_length=255,blank=True,default="Client")
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    objects = CustomUserManager()
    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        ordering = ["-id"]