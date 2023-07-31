from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile, ProfileType

# Register your models here.


# Para la web DJANGO ADMINISTRATION
class CustomUserAdmin(UserAdmin, admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone_number', 'date_joined')

    list_filter = ('date_joined',)

    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

    date_hierarchy = 'date_joined'  # Para que aparesca PRIMERO LOS USUARIOS.

    ordering = ('-id',)

    fieldsets = (
        (None, {
            "fields": ("username", "password")
        }
        ),
        (
            ("Información del usuario"), {
                'fields': ('first_name', 'last_name', 'email', 'phone_number')
            }
        ),
        (("Metadata"), {
            'fields': ('last_login', 'date_joined')
        }
        ),
    )


class ProfileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_type')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_type')


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(ProfileType)
admin.site.register(Profile)
