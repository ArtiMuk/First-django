# Generated by Django 4.2.3 on 2023-08-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_adverts', '0006_alter_advertisement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Категория'),
        ),
    ]
