from django.contrib import admin

from watchlist.models import Watchlist


@admin.register(Watchlist)
class AdminWatchlist (admin.ModelAdmin):
    pass