# Generated by Django 3.2.9 on 2022-01-06 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='author_user',
            new_name='author_user_id',
        ),
    ]
