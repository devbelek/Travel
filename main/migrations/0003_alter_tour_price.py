# Generated by Django 5.0.7 on 2024-07-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_placetolive_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
