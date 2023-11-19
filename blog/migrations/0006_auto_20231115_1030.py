# Generated by Django 3.2.23 on 2023-11-15 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20231113_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogentry',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='entry_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='blogentry',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='entries', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='review',
            field=models.CharField(default='', max_length=50),
        ),
    ]
