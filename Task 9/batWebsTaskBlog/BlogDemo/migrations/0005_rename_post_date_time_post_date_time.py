# Generated by Django 5.0 on 2023-12-27 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogDemo', '0004_remove_post_post_date_post_post_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_date_time',
            new_name='date_time',
        ),
    ]
