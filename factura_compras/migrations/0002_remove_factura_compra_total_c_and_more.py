# Generated by Django 4.2.2 on 2023-12-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura_compras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura_compra',
            name='total_c',
        ),
        migrations.AlterField(
            model_name='factura_compra',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
    ]
