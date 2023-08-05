# Generated by Django 4.2.2 on 2023-06-29 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='Publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
