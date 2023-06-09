# Generated by Django 4.2.1 on 2023-05-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_synopsis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='synopsis',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='year',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
