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


class JobPosting(models.Model):
    content=models.CharField(_('content'),max_length=255,blank=True,null=True)
    description=models.TextField(_('description'),blank=True,null=True)
    qualification=models.TextField(_('qualification'),blank=True,null=True)
    position=models.TextField(_('position'),blank=True,null=True)
    department=models.TextField(_('department'),blank=True,null=True)
    date_created=models.DateTimeField(_('date_created'), null=False,blank=False,default=timezone.now)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
