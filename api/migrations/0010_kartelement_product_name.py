# Generated by Django 4.1.1 on 2022-09-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_kartelement_color_kartelement_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='kartelement',
            name='product_name',
            field=models.CharField(blank=True, default=None, max_length=225, null=True),
        ),
    ]