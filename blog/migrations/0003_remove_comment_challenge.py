# Generated by Django 4.2.16 on 2024-09-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
