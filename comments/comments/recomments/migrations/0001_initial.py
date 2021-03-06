# Generated by Django 3.1.1 on 2020-12-08 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodcomments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReFoodComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=500)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodcomments.foodcomment')),
            ],
        ),
    ]
