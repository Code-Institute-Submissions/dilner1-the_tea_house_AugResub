# Generated by Django 3.2.13 on 2022-07-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220714_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='f_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='l_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
