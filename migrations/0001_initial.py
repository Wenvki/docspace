# Generated by Django 2.0.6 on 2018-07-02 16:36

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(blank=True, max_length=64, verbose_name='用户昵称')),
                ('mobile', models.CharField(blank=True, max_length=16, verbose_name='手机号码')),
                ('website', models.URLField(blank=True, null=True, verbose_name='个人站点')),
                ('role', models.SlugField(default='editor', verbose_name='用户角色')),
                ('resume', models.TextField(blank=True, null=True, verbose_name='个人简介')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'ds_users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('content', simditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
                ('comment_status', models.SlugField(choices=[('open', '开放'), ('closed', '关闭')], default='open', verbose_name='会话状态')),
                ('mime_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='MIME类型')),
                ('post_type', models.SlugField(choices=[('post', '文章'), ('page', '页面'), ('attachment', '附件')], default='post', max_length=64, verbose_name='文章类型')),
                ('status', models.SlugField(choices=[('draft', '草稿'), ('trash', '已回收'), ('published', '已发布'), ('pending', '等待复审'), ('inherit', '继承'), ('auto-draft', '自动保存')], default='auto-draft', verbose_name='状态')),
                ('views_num', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('comment_num', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'ds_articles',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('author_name', models.CharField(max_length=12, verbose_name='姓名')),
                ('author_email', models.EmailField(max_length=36, verbose_name='电子邮件')),
                ('author_url', models.URLField(blank=True, null=True, verbose_name='站点')),
                ('author_ip', models.GenericIPAddressField(verbose_name='IP地址')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('approved', models.SlugField(default='yes', verbose_name='是否被批准')),
                ('agent', models.TextField(blank=True, null=True, verbose_name='Agent')),
                ('notify', models.SlugField(default='push', verbose_name='通知')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docspace_comment_article', to='docspace.Article', verbose_name='所属文章')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docspace_comment_parent', to='docspace.Comment', verbose_name='父级ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'ds_comments',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='link_name', max_length=255, verbose_name='名称')),
                ('url', models.URLField(db_column='link_url', max_length=255, verbose_name='Web地址')),
                ('image', models.CharField(blank=True, db_column='link_image', max_length=255, null=True, verbose_name='图像地址')),
                ('target', models.CharField(db_column='link_target', default='_blank', max_length=25, verbose_name='打开方式')),
                ('description', models.CharField(blank=True, db_column='link_description', max_length=255, null=True, verbose_name='链接描述')),
                ('visible', models.CharField(blank=True, db_column='link_visible', max_length=20, null=True)),
                ('rating', models.IntegerField(db_column='link_rating', default=0, verbose_name='评分')),
                ('updated', models.DateTimeField(blank=True, db_column='link_updated', null=True)),
                ('rel', models.CharField(db_column='link_rel', default='friend', max_length=255, verbose_name='链接关系(XFN)')),
                ('notes', models.TextField(blank=True, db_column='link_notes', null=True, verbose_name='备注')),
                ('rss', models.CharField(blank=True, db_column='link_rss', max_length=255, null=True, verbose_name='RSS地址')),
                ('owner', models.ForeignKey(blank=True, db_column='link_owner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '链接',
                'verbose_name_plural': '链接',
                'db_table': 'ds_links',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='键名')),
                ('value', models.TextField(verbose_name='键值')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='object id')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docspace_metadata_content_type', to='contenttypes.ContentType', verbose_name='content type')),
            ],
            options={
                'verbose_name': '元数据',
                'verbose_name_plural': '元数据',
                'db_table': 'ds_metadatas',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='键名')),
                ('value', models.TextField(verbose_name='键值')),
                ('autoload', models.BooleanField(default=False, verbose_name='自动加载')),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
                'db_table': 'ds_options',
            },
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='键名')),
                ('value', models.TextField(verbose_name='键值')),
                ('mark', models.SlugField(choices=[('tag', '标签'), ('category', '分类'), ('link', '链接'), ('file', '文件'), ('photo', '图像'), ('audio', '音频'), ('video', '视频'), ('special', '专题')], default='tag', max_length=12, verbose_name='标记')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docspace_taxonomy_parent', to='docspace.Taxonomy', verbose_name='父级ID')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'ds_taxonomys',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, limit_choices_to={'mark': 'category'}, related_name='docspace_article_category', to='docspace.Taxonomy', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docspace_article_parent', to='docspace.Article', verbose_name='父级ID'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'mark': 'tag'}, related_name='docspace_article_tags', to='docspace.Taxonomy', verbose_name='标签'),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
            ],
            options={
                'verbose_name': '媒体',
                'verbose_name_plural': '媒体',
                'proxy': True,
                'indexes': [],
            },
            bases=('docspace.article',),
        ),
    ]
