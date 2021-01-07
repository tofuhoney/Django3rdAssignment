from django.contrib import admin
from . import models

"""
Here are the models you have to create:

"""


@admin.register(models.Category)
class categoriesadmin(admin.ModelAdmin):
    """Category Admin Definition"""

    list_display = ("name", "kind")

    list_filter = ("kind",)
