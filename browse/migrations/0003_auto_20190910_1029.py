# Generated by Django 2.2.1 on 2019-09-10 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0002_file_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='File',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='Genre',
            new_name='genre',
        ),
    ]
