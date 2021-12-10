from django.contrib import admin
from .models import Course, Lesson, Material


# altera como o curso irá ser mostrado no django admin
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'ministrante', 'get_create_at', 'status')
    search_fields = ('course_title', 'ministrante')
    list_filter = ('course_title',)
    date_hierarchy = 'create_at'

    #define formato DD/MM/YYYY para o field create_at
    def get_create_at(self, obj):
        if obj.create_at:
            return obj.create_at.strftime('%d/%m/%Y')


# altera como o lesson irá ser mostrado no django admin
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_title', 'course', 'synopsis', 'get_create_at')
    search_fields = ('lesson_title', 'course')
    list_filter = ('lesson_title',)
    date_hierarchy = 'create_at'

    def get_create_at(self, obj):
        if obj.create_at:
            return obj.create_at.strftime('%d/%m/%Y')


# altera como o material irá ser mostrado no django admin
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_title', 'course', 'file', 'get_upload_at')
    search_fields = ('material_title', 'course')
    list_filter = ('material_title',)
    date_hierarchy = 'upload_at'

    def get_upload_at(self, obj):
        if obj.upload_at:
            return obj.upload_at.strftime('%d/%m/%Y')

