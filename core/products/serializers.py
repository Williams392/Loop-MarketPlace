# (3) -> actualizar para la importación en el archivo views.py

# serializers.py

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


""" 
Ejemplo de JSON

GET:
{
  "product": "Yogurt LAIVE",
  "brand": "LAIVE",
  "price": 12,
  "description": "gurt con cultivos probióticos"
}

POST / PUT:

{
    "product": "Leche",
    "price": 3,
    "description": "Me encantó la película"
}

"""
