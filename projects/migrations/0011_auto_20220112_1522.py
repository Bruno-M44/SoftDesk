# Generated by Django 3.2.9 on 2022-01-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_rename_author_user_id_projects_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributors',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='contributors',
            name='role',
        ),
    ]
