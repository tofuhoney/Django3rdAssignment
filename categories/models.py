from django.db import models

from core import models as core_models

"""
Here are the models you have to create:
- Category
  name
  kind (book/movie/both)
"""


class Category(core_models.TimestampedModel):
    """ Category definition Class"""

    BOOK = "Book"
    MOVIE = "Movie"
    BOTH = "Both"
    CHOICES = ((BOOK, "Book"), (MOVIE, "Movie"), (BOTH, "Both"))

    name = models.CharField(max_length=20)
    kind = models.CharField(choices=CHOICES, max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
