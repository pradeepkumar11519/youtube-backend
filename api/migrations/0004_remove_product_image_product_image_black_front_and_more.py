# Generated by Django 4.1.1 on 2022-09-25 05:08

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_black_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_blue_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_dark_blue_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_gray_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_green_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_light_blue_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_maroon_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_red_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_white_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
        migrations.AddField(
            model_name='product',
            name='image_yellow_front',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=api.models.upload_photo),
        ),
    ]
