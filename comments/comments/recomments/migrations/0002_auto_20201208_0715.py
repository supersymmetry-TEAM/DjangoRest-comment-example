# Generated by Django 3.1.1 on 2020-12-08 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refoodcomment',
            old_name='comment_id',
            new_name='comment',
        ),
    ]