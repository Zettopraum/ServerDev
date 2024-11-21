from django.contrib import admin

from genres.models import Genres


@admin.register(Genres)
class AdminGenres (admin.ModelAdmin):
    pass