# Generated by Django 4.2.2 on 2023-07-23 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='topic',
            new_name='topicc',
        ),
    ]
