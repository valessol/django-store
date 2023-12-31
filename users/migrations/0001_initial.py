# Generated by Django 3.2.23 on 2023-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('entries', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('biography', models.CharField(max_length=300)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
    ]
