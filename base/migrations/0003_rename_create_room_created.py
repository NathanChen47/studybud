# Generated by Django 5.1.5 on 2025-02-06 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='create',
            new_name='created',
        ),
    ]
