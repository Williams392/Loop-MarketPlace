# (3) models.py

from django.db import models
from django.conf import settings


class Product(models.Model):

    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Photo(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='product_photos')


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    '''
    YO ise esto:
    product = models.CharField(max_length=255, unique=True)

    brand = models.CharField(
        max_length=255, unique=True, null=True, default=None)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)

    image = models.FileField(upload_to='products/',
                             null=True, blank=True)

    # image = models.ImageField()
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.product
    '''


'''
1. Actualizar las migraciones y aplicar los cambios:
_ python manage.py makemigrations
_ python manage.py migrate
'''


# 2. Para visualizar en DJANGO administration:
# _ amdmin.py

# . Imagenes en Django:
# _ pipenv install Pillow
