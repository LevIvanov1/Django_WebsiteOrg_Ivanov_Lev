# Generated by Django 4.2 on 2025-05-17 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site_company', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
