from django.contrib import admin

from recommendations.models import Recommendations


@admin.register(Recommendations)
class AdminRecommendations (admin.ModelAdmin):
    pass