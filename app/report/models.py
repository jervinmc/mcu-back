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


class Report(models.Model):
    announcement_views = models.IntegerField(_('announcement_views'),default=0.0)
    event_views = models.IntegerField(_('event_views'),default=0.0)
    posting_views = models.IntegerField(_('posting_views'),default=0.0)
    class Meta:
        ordering = ["-id"]
