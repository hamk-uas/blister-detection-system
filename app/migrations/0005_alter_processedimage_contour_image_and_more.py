# Generated by Django 5.1 on 2024-10-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedimage',
            name='contour_image',
            field=models.ImageField(blank=True, null=True, upload_to='folders/contours/'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='detected_blisters_image',
            field=models.ImageField(blank=True, null=True, upload_to='folders/detection/'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='rectangles_image',
            field=models.ImageField(blank=True, null=True, upload_to='folders/rectangles/'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='region_image',
            field=models.ImageField(blank=True, null=True, upload_to='folders/regions/'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='removal_image',
            field=models.ImageField(blank=True, null=True, upload_to='folders/removals/'),
        ),
    ]