from django.db import models

from core import models as core_models
from categories import models as cate_models
from people import models as people_models

"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""


class movie(core_models.TimestampedModel):
    """ Movie model Definition """

    title = models.CharField(max_length=30)
    year = models.DateField(blank=True, null=True)
    cover_image = models.FileField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    category = models.ManyToManyField(cate_models.Category, blank=True)
    director = models.ForeignKey(
        people_models.Person,
        related_name="director",
        on_delete=models.SET_NULL,
        null=True,
    )
    cast = models.ManyToManyField(people_models.Person, related_name="cast", blank=True)

    def __str__(self):
        return self.title
