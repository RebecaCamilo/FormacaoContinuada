from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, matricula, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, matricula, password, **other_fields)

    def create_user(self, email, first_name, matricula, password, **other_fields):

        if not email:
            raise ValueError(('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, matricula=matricula, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    matricula = models.CharField(max_length=30, unique=True)
    curso = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14) #(00)00000-0000
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    #It is a string describing the name of the field on the User model that is used as the unique identifier. The field must be unique (i.e., have unique=True set in its definition).
    USERNAME_FIELD = 'email'
    #It is a list of the field names that will be prompted when creating a user via the createsuperuser command.
    REQUIRED_FIELDS = ['matricula', 'first_name']
    
    
    def __str__(self):
        return self.first_name

    
    


'''
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30,  blank=True, null=True)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=30, unique=True)
    curso = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14) #(00)00000-0000

    #It is a string describing the name of the field on the User model that is used as the unique identifier. The field must be unique (i.e., have unique=True set in its definition).
    USERNAME_FIELD = 'email'
    #It is a list of the field names that will be prompted when creating a user via the createsuperuser command.
    REQUIRED_FIELDS = ['first_name','last_name', 'matricula', 'curso',  'telefone']
'''


'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on_delete=models.CASCADE, se o User for deletado, seu respectivo UserProfile tbm será
    matricula = models.CharField(max_length=30)
    curso = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14) #(00)00000-0000
'''
