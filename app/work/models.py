from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Work(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    company_name=models.CharField(_('company_name'),max_length=255,blank=True,null=True)
    position=models.CharField(_('position'),max_length=255,blank=True,null=True)
    field=models.CharField(_('field'),max_length=255,blank=True,null=True)
    date_joined=models.DateTimeField(_('date_joined'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
