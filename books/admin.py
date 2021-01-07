from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    """Book Admin Definition"""

    list_display = ("title", "year", "category", "cover_image", "rating", "writer")

    list_filter = ("category", "writer")
