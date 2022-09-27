# Generated by Django 4.1.1 on 2022-09-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_order_ordereditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at_time',
            field=models.CharField(blank=True, default='5:23:28 pm', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at_time',
            field=models.CharField(blank=True, default='5:23:28 pm', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='price',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]