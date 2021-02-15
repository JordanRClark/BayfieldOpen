from django.contrib import admin

from . import models

class ScoreInline(admin.TabularInline):
    model = models.Score

class RoundAdmin(admin.ModelAdmin):
    inlines = [
        ScoreInline
    ]
    list_display = (
        'id',
    )

    search_fields = (
        'id',
        'user__email',
    )

class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )

    search_fields = (
        'id',
        'hole__course__name',
        'hole_id',
        'round__user__email',
    )

admin.site.register(models.Round, RoundAdmin)
admin.site.register(models.Score, ScoreAdmin)
