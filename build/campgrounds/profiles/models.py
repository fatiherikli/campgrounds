from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import smart_unicode

from campgrounds.places.models import Campground
from campgrounds.profiles.constants import NOTIFICATION_TYPE_APPROVAL, NOTIFICATION_TYPES


class User(AbstractUser):
    """Custom user model"""
    full_name = property(AbstractUser.get_full_name)

    def gravatar(self, size=80):
        import urllib, hashlib
        return "http://www.gravatar.com/avatar/%(hash)s?%(parameters)s" % {
            'hash': hashlib.md5(self.email.lower()).hexdigest(),
            'parameters': urllib.urlencode({'s':str(size)})
        }


class Notification(models.Model):
    """Holds the notifications of user. The sender field will be empty
    for system notifications."""
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="notifications")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    is_seen = models.BooleanField(default=False)
    object_id = models.IntegerField()

    model_mapping = {
        NOTIFICATION_TYPE_APPROVAL: Campground
    }

    def __unicode__(self):
        return smart_unicode("%s -> %s" % (
            self.get_notification_type_display(), self.recipient))

    def get_absolute_url(self):
        """Returns the url of related object about notification"""
        model = self.model_mapping.get(self.notification_type)
        instance = model.objects.get(id=self.object_id)
        return instance.get_absolute_url()
