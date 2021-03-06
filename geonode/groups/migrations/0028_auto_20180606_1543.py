# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 15:43


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0027_auto_20180105_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcategory',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='groupcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='groupcategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='groups', to='groups.GroupCategory', verbose_name='Categories'),
        ),
    ]
