# Generated by Django 5.1.4 on 2024-12-21 18:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seanse', '0002_alter_film_options_alter_sala_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rezerwacja',
            options={'verbose_name_plural': 'Rezerwacje'},
        ),
        migrations.AlterField(
            model_name='rezerwacja',
            name='liczba_biletow',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Liczba biletów'),
        ),
        migrations.AlterField(
            model_name='rezerwacja',
            name='seans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rezerwacje', to='seanse.seans'),
        ),
    ]
