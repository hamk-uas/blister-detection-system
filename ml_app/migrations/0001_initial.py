# Generated by Django 5.1 on 2024-10-07 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_alter_processedimage_contour_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.JSONField()),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ml_result', to='app.image')),
            ],
        ),
    ]
