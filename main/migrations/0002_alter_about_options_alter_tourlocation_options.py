# Generated by Django 5.0.7 on 2024-07-23 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'O нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='tourlocation',
            options={'verbose_name': 'Локация', 'verbose_name_plural': 'Локации'},
        ),
    ]
