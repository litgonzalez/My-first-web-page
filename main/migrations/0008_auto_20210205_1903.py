# Generated by Django 3.1.5 on 2021-02-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_contacto_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='comentario',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario'),
        ),
        migrations.DeleteModel(
            name='Orden_compra',
        ),
    ]