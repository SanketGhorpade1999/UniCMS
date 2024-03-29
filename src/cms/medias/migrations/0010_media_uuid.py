# Generated by Django 3.2.13 on 2022-09-27 09:05

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    Media = apps.get_model('cmsmedias', 'Media')
    for media in Media.objects.all():
        media.uuid = uuid.uuid4()
        media.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmedias', '0009_alter_media_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='media',
            name='uuid',
            field=models.UUIDField(unique=True, editable=False)
        )
    ]
