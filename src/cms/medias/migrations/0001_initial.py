# Generated by Django 3.1.4 on 2021-01-15 11:24

import cms.medias.models
import cms.medias.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers

from cms.medias.settings import FILETYPE_ALLOWED

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('file_type', models.CharField(blank=True, choices=(lambda: FILETYPE_ALLOWED)(), max_length=256, null=True)),
                ('title', models.CharField(help_text='Media file title', max_length=60)),
                ('file', models.FileField(upload_to=cms.medias.models.context_media_path, validators=[cms.medias.validators.validate_file_extension, cms.medias.validators.validate_file_size, cms.medias.validators.validate_image_size_ratio])),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Media',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(max_length=1024)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediacollection_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediacollection_modified_by', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Media Collections',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MediaCollectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(blank=True, default=10, null=True)),
                ('is_active', models.BooleanField()),
                ('collection', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='cmsmedias.mediacollection')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediacollectionitem_created_by', to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='cmsmedias.media')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediacollectionitem_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Media Collection Items',
                'ordering': ['order'],
            },
        ),
    ]