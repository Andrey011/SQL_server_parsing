# Generated by Django 3.2.16 on 2022-11-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms_Of_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Form', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
