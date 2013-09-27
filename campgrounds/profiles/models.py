from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import smart_unicode


class User(AbstractUser):

    full_name = property(AbstractUser.get_full_name)

    def gravatar(self, size=80):
        import urllib, hashlib
        return "http://www.gravatar.com/avatar/%(hash)s?%(parameters)s" % {
            'hash': hashlib.md5(self.email.lower()).hexdigest(),
            'parameters': urllib.urlencode({'s':str(size)})
        }


NOTIFICATION_TYPES = (
    (1, 'Approved your campground.'),
)

class Notification(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name="notifications")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    is_seen = models.BooleanField(default=False)
    object_id = models.IntegerField()

    def __unicode(self):
        return smart_unicode("%s -> %s" % (self.get_notification_type_display(),
                                           self.recipient))
