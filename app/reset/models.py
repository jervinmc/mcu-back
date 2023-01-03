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


class Reset(models.Model):
    # request_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # enma = models.IntegerField(_('user_id'),default=0.0)
    # price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    # date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    # is_active=models.BooleanField(_('is_active'),default=True)
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
