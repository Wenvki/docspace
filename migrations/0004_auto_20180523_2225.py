# Generated by Django 2.0.3 on 2018-05-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docspace', '0003_auto_20180523_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views_num',
            field=models.PositiveIntegerField(default=75, verbose_name='阅读数'),
        ),
    ]
