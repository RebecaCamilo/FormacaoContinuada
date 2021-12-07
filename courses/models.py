from django.db import models


# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=150)
    #imagem
    ministrante = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    #function that returns the quantity of lessons that the couse have
    def get_num_lessons(self):
        return Lesson.objects.filter(couse=self).count()

    def __str__(self):
        return self.course_title


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    synopsis = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_title


class Material(models.Model):
    material_title = models.CharField(max_length=100)
    file = models.FileField() #upload_to='pdf/'
    course = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.material_title





