# Generated by Django 5.0.3 on 2024-03-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='sex',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=0, verbose_name='性别'),
            preserve_default=False,
        ),
    ]