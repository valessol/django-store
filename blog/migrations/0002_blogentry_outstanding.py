# Generated by Django 3.2.23 on 2023-11-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='outstanding',
            field=models.BooleanField(default=False),
        ),
    ]
