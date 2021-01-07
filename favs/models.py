from django.db import models

from core import models as core_models
from users import models as user_models
from books import models as book_models
from movies import models as movie_models

"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""


class FavList(core_models.TimestampedModel):
    """Model Favlist Definition"""

    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    books = models.ManyToManyField(book_models.Book, blank=True)
    movies = models.ManyToManyField(movie_models.movie, blank=True)
