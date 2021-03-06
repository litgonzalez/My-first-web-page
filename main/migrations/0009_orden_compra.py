# Generated by Django 3.1.5 on 2021-02-05 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210205_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_compra',
            fields=[
                ('orden', models.AutoField(primary_key=True, serialize=False)),
                ('metodopago', models.CharField(choices=[('DB', 'Débito'), ('CR', 'Crédito'), ('EF', 'Efectivo')], max_length=50, verbose_name='Método de pago')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.persona')),
                ('producto', models.ManyToManyField(help_text='Selecciona tus productos manteniendo CTRL presionado', to='main.Producto')),
            ],
            options={
                'verbose_name_plural': 'Órdenes de compra',
            },
        ),
    ]
