# Generated by Django 4.1.7 on 2023-05-01 13:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_post_tags'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentList',
            new_name='Comment',
        ),
    ]