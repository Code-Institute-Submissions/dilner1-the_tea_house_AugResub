# Generated by Django 3.2.13 on 2022-07-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_basketorderitems_basketitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='order_number',
            field=models.CharField(max_length=30),
        ),
    ]
