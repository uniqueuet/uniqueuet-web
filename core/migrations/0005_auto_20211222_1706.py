# Generated by Django 2.2.14 on 2021-12-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211130_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SU', 'Sun Care'), ('SK', 'Skin Care'), ('HA', 'Hair Care'), ('BO', 'Body Care'), ('PF', 'Perfume'), ('DC', 'Decorative Cosmetics'), ('OR', 'Oral Care')], max_length=2),
        ),
    ]
