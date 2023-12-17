# Generated by Django 4.2.2 on 2023-12-17 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factura_ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateField()),
                ('telefono', models.PositiveIntegerField(null=True)),
                ('factura_v', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura_ventas.factura_venta')),
            ],
        ),
    ]
