# Generated by Django 3.2.23 on 2023-11-17 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment_related_to'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
