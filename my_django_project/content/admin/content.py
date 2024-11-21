from django.contrib import admin
from content.models.content import Content



@admin.register(Content)
class AdminContent(admin.ModelAdmin):
    pass