from django.contrib import admin
from django.contrib.admin import ModelAdmin

from campgrounds.places.models import Campground


class CampgroundAdmin(ModelAdmin):
    pass


admin.site.register(Campground, CampgroundAdmin)