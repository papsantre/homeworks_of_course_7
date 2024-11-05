from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    list_filter = ("title",)
    search_fields = (
        "title",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ("title",)
