from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.utils.encoding import smart_unicode


ENTRY_TYPE_TEXT = 0
ENTRY_TYPE_PHOTO = 1
ENTRY_TYPE_LINK = 2
ENTRY_TYPES = (
    (0, 'Text'),
    (1, 'Photo'),
    (2, 'Link'),
)


class Entry(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    entry_type =  models.IntegerField(choices=ENTRY_TYPES,
                                      default=ENTRY_TYPE_TEXT)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="wall", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.content)
