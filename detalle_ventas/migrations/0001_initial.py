# Generated by Django 4.2.2 on 2023-12-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factura_ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('factura_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura_ventas.factura_venta')),
            ],
        ),
    ]
