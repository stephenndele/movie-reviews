# Generated by Django 2.1.7 on 2021-03-27 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movies',
            new_name='movie',
        ),
    ]
