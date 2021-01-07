from django.db import models


# Create your models here.
class TimestampedModel(models.Model):
    """Abstract Model extend for created, updated time"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
