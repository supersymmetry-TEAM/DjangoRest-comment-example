# Generated by Django 3.1.1 on 2020-12-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomments', '0005_auto_20201213_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refoodcomment',
            name='is_down_list',
            field=models.TextField(default=','),
        ),
        migrations.AlterField(
            model_name='refoodcomment',
            name='is_up_list',
            field=models.TextField(default=','),
        ),
    ]
