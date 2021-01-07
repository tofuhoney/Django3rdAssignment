from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.movie)
class MovieAdmin(admin.ModelAdmin):
    """Movie Admin Definition"""

    list_display = ("title", "director", "year", "cover_image", "rating")
