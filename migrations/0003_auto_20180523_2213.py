# Generated by Django 2.0.3 on 2018-05-23 22:13

from django.db import migrations, models
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('docspace', '0002_auto_20180516_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_num',
            field=models.PositiveIntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AddField(
            model_name='article',
            name='views_num',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=simditor.fields.RichTextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='mark',
            field=models.SlugField(choices=[('tag', '标签'), ('category', '分类'), ('link', '链接'), ('file', '文件'), ('photo', '图像'), ('audio', '音频'), ('video', '视频'), ('special', '专题')], default='tag', max_length=12, verbose_name='标记'),
        ),
    ]
