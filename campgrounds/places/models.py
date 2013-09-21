from django.conf import settings
from django.contrib.gis.db import models
from django.utils.encoding import smart_unicode

from markitup.fields import MarkupField


class Campground(models.Model):
    """Holds camp areas"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    city = models.CharField(max_length=255)
    location = models.PointField()
    address = models.TextField(blank=True, null=True)
    description = MarkupField()
    directions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return smart_unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return 'place-detail', [self.slug]


class Rating(models.Model):
    """Holds the ratings of a campground"""
    campground = models.ForeignKey(Campground)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    vote = models.IntegerField()
    comment = models.TextField()

    def __unicode__(self):
        return smart_unicode(self.comment)


class Photo(models.Model):
    """Holds photos of a campground"""
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return smart_unicode(self.title)