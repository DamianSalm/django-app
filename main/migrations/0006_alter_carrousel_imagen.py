# Generated by Django 4.1.1 on 2022-10-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_carrousel_foto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrousel',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img_carousel'),
        ),
    ]
