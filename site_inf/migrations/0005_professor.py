# Generated by Django 5.2 on 2025-05-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_inf', '0004_exaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('area_atuacao', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
