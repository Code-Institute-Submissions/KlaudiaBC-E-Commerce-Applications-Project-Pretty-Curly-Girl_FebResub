# Generated by Django 4.0 on 2023-01-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_order_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
