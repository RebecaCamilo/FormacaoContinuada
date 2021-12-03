from django.http import response
from rest_framework import serializers, viewsets
from ..models import Course, Lesson, Material
from .serializers import CourseSerializer
from .serializers import LessonSerializer
from .serializers import MaterialSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['id'])
        courses = CourseSpecs.objects.filter(id = params['id'])
        serializer = CourseSerializer(courses, many=True)
        return response.ResponseHeaders(serializer.data)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer



