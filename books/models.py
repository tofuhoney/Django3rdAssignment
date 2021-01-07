from django.db import models

from core import models as core_models
from categories import models as cate_models
from people import models as people_models

"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""


class Book(core_models.TimestampedModel):
    """Book Class Definition"""

    title = models.CharField(max_length=20)
    year = models.IntegerField(default=1900)
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField()

    category = models.ForeignKey(cate_models.Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(people_models.Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
