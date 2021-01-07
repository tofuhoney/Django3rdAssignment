from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    """Person Admin Definition"""

    list_display = ("name", "kind", "photo")

    list_filter = ("kind",)
