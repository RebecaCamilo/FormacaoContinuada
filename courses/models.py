from django.db import models


# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=150)
    ministrante = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    #acrescetar um field para por imagem no card

    #function that returns the quantity of lessons that the couse have
    def get_num_lessons(self):
        return Lesson.objects.filter(couse=self).count()

    def __str__(self):
        return self.course_title


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    #cria relação de muitas lessons pra um curso (um curso pode ter 1 ou varias aulas). CASCADE = quando o curso for deletado, as aulas(lessons) conectadas com ele também serão
    synopsis = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_title


class Material(models.Model):
    material_title = models.CharField(max_length=100)
    file = models.FileField()   #pode-se usar "upload_to='pdf/'" como parâmentro, mas restringiria o upload a apenas pdf
    course = models.ForeignKey(Lesson, on_delete=models.CASCADE)    #cria relação de muitos materials pra uma lesson (uma aula pode ter 1 ou varios materiais)
    upload_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.material_title





