# Generated by Django 5.0.7 on 2024-07-23 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_guides'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guides',
            options={'verbose_name': 'Список гидов', 'verbose_name_plural': 'Список гидов'},
        ),
    ]
