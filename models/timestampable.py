from django.db import models
from django.utils.translation import ugettext_lazy as _


# Timestampable tracks 'created_at' and 'updated_at' fields.
class Timestampable(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        abstract = True
