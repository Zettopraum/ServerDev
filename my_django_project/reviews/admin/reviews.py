from django.contrib import admin

from reviews.models import Reviews


@admin.register(Reviews)
class AdminReviews (admin.ModelAdmin):
    pass