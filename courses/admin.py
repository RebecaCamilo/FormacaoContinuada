from django.contrib import admin
from .models import Course, Lesson, Material


# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'ministrante', 'get_create_at', 'status')
    search_fields = ('course_title', 'ministrante')
    list_filter = ('course_title',)
    date_hierarchy = 'create_at'

    def get_create_at(self, obj):
        if obj.create_at:
            return obj.create_at.strftime('%d/%m/%Y')


# admin.site.register(Lesson)
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_title', 'course', 'synopsis', 'get_create_at')
    search_fields = ('lesson_title', 'course')
    list_filter = ('lesson_title',)
    date_hierarchy = 'create_at'

    def get_create_at(self, obj):
        if obj.create_at:
            return obj.create_at.strftime('%d/%m/%Y')


# admin.site.register(Material)
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_title', 'couse', 'file', 'get_upload_at')
    search_fields = ('material_title', 'couse')
    list_filter = ('material_title',)
    date_hierarchy = 'upload_at'

    def get_upload_at(self, obj):
        if obj.upload_at:
            return obj.upload_at.strftime('%d/%m/%Y')

