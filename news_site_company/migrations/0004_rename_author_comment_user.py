# Generated by Django 4.2 on 2025-05-17 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site_company', '0003_rename_user_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
