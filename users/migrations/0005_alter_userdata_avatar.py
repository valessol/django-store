# Generated by Django 3.2.23 on 2023-11-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20231113_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='avatares'),
        ),
    ]
