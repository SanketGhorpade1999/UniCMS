# Generated by Django 3.2.3 on 2021-05-31 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmsmedias', '0008_alter_media_file'),
        ('cmspublications', '0015_auto_20210531_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationMediaCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(blank=True, default=10, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cmsmedias.mediacollection')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publicationmediacollection_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publicationmediacollection_modified_by', to=settings.AUTH_USER_MODEL)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmspublications.publication')),
            ],
            options={
                'verbose_name_plural': 'Publication Media Collection',
            },
        ),
        migrations.DeleteModel(
            name='PublicationGallery',
        ),
    ]