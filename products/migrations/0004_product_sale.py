# Generated by Django 3.2.16 on 2022-11-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='Product',
            name='sale',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]