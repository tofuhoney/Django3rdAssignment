from django.db import models
from core import models as core_models

"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""


class Person(core_models.TimestampedModel):
    """ Class Person Definition """

    ACTOR = "Actor"
    DIRECTOR = "Director"
    WRITER = "Writer"
    KIND_CHOICES = ((ACTOR, "Actor"), (DIRECTOR, "Director"), (WRITER, "Writer"))
    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KIND_CHOICES, default=ACTOR, max_length=10)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Person"
