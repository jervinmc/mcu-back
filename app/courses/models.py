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


class Courses(models.Model):
    user_id = models.IntegerField(_('no_people'),default=0.0)
    course=models.CharField(_('course'),max_length=255,blank=True,null=True)
    year_graduated=models.DateTimeField(_('year_graduated'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
