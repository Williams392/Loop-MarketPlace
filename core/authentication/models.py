from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    # ordenarse por la clave primaria (pk).
    class Meta:
        ordering = ['pk']

    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=130, unique=True, null=False)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    pass

    def __str__(self):
        return f"{self.username} - {self.email}"


class ProfileType(models.Model):
    """
    Catálogo para manejar los tipos de perfiles:
    1. Vendedor
    2. Comprador
    """
    profile_type = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_type = models.ForeignKey(ProfileType, on_delete=models.PROTECT)


'''
1. Actualizar las migraciones y aplicar los cambios:
_ python manage.py makemigrations
_ python manage.py migrate
'''
