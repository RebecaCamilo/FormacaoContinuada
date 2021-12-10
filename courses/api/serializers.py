from rest_framework import serializers
from ..models import Course, Lesson, Material

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_title', 'ministrante', 'status')    #Especifica os fields que aparecerão na API


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('lesson_title', 'course', 'synopsis', 'description')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('material_title', 'file', 'course')


