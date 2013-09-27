from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from campgrounds.profiles.models import Notification


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Notification)
