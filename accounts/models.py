from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    # metodo que cria um super user
    def create_superuser(self, email, name, cpf, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, cpf, password, **other_fields)

    # metodo que cria um usuario comum (nao super)
    def create_user(self, email, name, cpf, password, **other_fields):
        if not email:
            raise ValueError(('You must have an email address'))
        if not name:
            raise ValueError(('You must have a first name'))
        if not cpf:
            raise ValueError(('You must have an cpf'))

        user = self.model(
            email=self.normalize_email(email), 
            name=name, 
            cpf=cpf, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


#Classe User criada extendendo o AbstractBaseUser (para acrescentar campos necessários especificamente para esta aplicação) e PermissionsMixin (ACHO que envolve as variaveis is_staff, is_superuser e is_active)
class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=150) 
    course = models.CharField(max_length=255, verbose_name="Curso vinculado")
    email = models.EmailField(('email address'), unique=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF") 
    password2 = models.CharField(max_length=150, verbose_name="Confirme a senha")
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    #para criar objetos deste model, faz-se por meio da classe CustomAccountManager, na qual sobrescrevemos e metodos (create_superuser e create_user)
    objects = CustomAccountManager()

    #It is a string describing the name of the field on the User model that is used as the unique identifier. The field must be unique (i.e., have unique=True set in its definition).
    USERNAME_FIELD = 'email'
    #It is a list of the field names that will be prompted when creating a user via the createsuperuser command.
    REQUIRED_FIELDS = ['cpf', 'name']
    
    
    def __str__(self):
        return self.name

