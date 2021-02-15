from django.contrib import admin

from . import models

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'id',
        'name',
    )

class HoleStatsInline(admin.TabularInline):
    model = models.HoleTeeStats


class HoleAdmin(admin.ModelAdmin):
    inlines = [
        HoleStatsInline
    ]
    list_display = (
        'id',
        'course',
    )

    search_fieldds = (
        'id',
        'course__name',
    )

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Hole, HoleAdmin)
