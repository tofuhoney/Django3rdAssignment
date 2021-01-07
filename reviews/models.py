from django.db import models
from core import models as core_models
from movies import models as movie_models
from books import models as book_models
from users import models as user_models

"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""


class Review(core_models.TimestampedModel):
    """ Class Review Definition"""

    text = models.TextField(max_length=300)
    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        movie_models.movie, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        book_models.Book, on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField()
