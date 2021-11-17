from django.contrib import admin
from .models import User

#admin.site.register(User)
from django.contrib.auth.admin import UserAdmin

#cria a classe UserAdminConfig extendida da UserAdmin (modifica a forma de mostrar os objetos user no admin do django)
class UserAdminConfig(UserAdmin):
    model = User
    list_filter = ('email', 'cpf', 'first_name', 'password', 'is_active', 'is_staff')
    search_fields = ('email', 'cpf', 'first_name', 'password',)
    ordering = ('-start_date',)
    list_display = ('email', 'cpf', 'first_name', 'password',
                    'is_active', 'is_staff')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    
admin.site.register(User, UserAdminConfig)

