# Generated by Django 3.2.23 on 2023-11-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20231116_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='related_to',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
