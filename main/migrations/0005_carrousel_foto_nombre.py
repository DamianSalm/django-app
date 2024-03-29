# Generated by Django 4.1.1 on 2022-10-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=255)),
                ('imagen', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.AddField(
            model_name='foto',
            name='nombre',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
