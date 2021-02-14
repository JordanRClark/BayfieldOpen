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


class HoleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'par',
        'course',
    )

    search_fieldds = (
        'id',
        'course__name',
    )

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Hole, HoleAdmin)
