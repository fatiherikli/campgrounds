# coding=utf-8
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.encoding import smart_unicode
from django.utils.text import slugify

from markitup.fields import MarkupField
from campgrounds.places.managers import ActiveManager


class Campground(models.Model):
    """Holds camp areas"""
    title = models.CharField(max_length=255, verbose_name="Başlık")
    slug = models.SlugField()
    city = models.CharField(max_length=255, verbose_name="Şehir")
    location = models.PointField(verbose_name="Konum")
    description = MarkupField(verbose_name="Açıklama")
    directions = models.TextField(blank=True, null=True,
        verbose_name="Nasıl Gidilir")
    image = models.ImageField(
        upload_to="uploads", blank=True, null=True,
        verbose_name="Kapak Fotoğrafı")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    features = models.ManyToManyField(
        "places.Feature", blank=True, null=True, verbose_name="Özellikler",
        help_text="Markdown formatında yazabilirsiniz.")
    is_active = models.BooleanField(default=False)

    objects = ActiveManager()

    def __unicode__(self):
        return smart_unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return 'place-detail', [self.slug]

    @classmethod
    def unique_slug(cls, title, count=0):
        """Generates unique slug key by the given title."""
        slug = slugify(title)
        if count:
            slug += "-%s" % count
        if cls.objects.filter(slug=slug).exists():
            return cls.unique_slug(title, count+1)
        return slug

    @property
    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ""


class Feature(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="icons", blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)


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
