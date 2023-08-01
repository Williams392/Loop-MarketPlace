# 4

from django.contrib import admin
from .models import Product, Photo, Tag, Category


class PhotoInline(admin.StackedInline):
    model = Photo


class TagInline(admin.TabularInline):
    model = Tag.product_set.through


class CategoryInline(admin.TabularInline):
    model = Category.product_set.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, TagInline, CategoryInline]


admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Category)


'''
    YO ise esto:
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'price', 'description', 'image')
    ordering = ('-id',)


admin.site.register(Product, ProductAdmin)
'''


# Para visualizal todos los dantos en el Django administration
'''
. search_fields = campos_de_búsqueda
. list_display = mostrar_lista
. list_filter  = lista_filtro
'''
