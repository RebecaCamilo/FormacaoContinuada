'''from django.contrib import admin
from .models import User

admin.site.register(User)'''


from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'matricula', 'first_name', 'password',)
    list_filter = ('email', 'matricula', 'first_name', 'password', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'matricula', 'first_name', 'password',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'matricula', 'first_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

'''    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'matricula', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )'''


admin.site.register(User, UserAdminConfig)