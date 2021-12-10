from rest_framework import viewsets
from ..models import Course, Lesson, Material
from .serializers import CourseSerializer
from .serializers import LessonSerializer
from .serializers import MaterialSerializer
from rest_framework.filters import SearchFilter


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter]    #cria o filtro de busca
    search_fields = ['course_title']    #define os fields a serem buscados no filtro

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [SearchFilter]
    search_fields = ['lesson_title', 'synopsis']

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer



