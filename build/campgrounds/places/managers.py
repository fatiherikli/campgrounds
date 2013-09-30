from django.contrib.gis.db import models


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)