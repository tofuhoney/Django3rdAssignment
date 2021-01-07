from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):
    """FavList admin Definition"""

    list_display = ("created_by",)
