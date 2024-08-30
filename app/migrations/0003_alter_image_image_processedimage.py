# Generated by Django 5.1 on 2024-08-17 12:57

import app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_folder_created_at_alter_folder_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=app.models.upload_to),
        ),
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contour_image', models.ImageField(blank=True, null=True, upload_to='contours/')),
                ('region_image', models.ImageField(blank=True, null=True, upload_to='regions/')),
                ('rectangles_image', models.ImageField(blank=True, null=True, upload_to='rectangles/')),
                ('removal_image', models.ImageField(blank=True, null=True, upload_to='removals/')),
                ('detected_blisters_image', models.ImageField(blank=True, null=True, upload_to='detection/')),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('original_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processed_images', to='app.image')),
            ],
        ),
    ]