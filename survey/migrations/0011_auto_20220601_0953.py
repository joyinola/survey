# Generated by Django 3.2.13 on 2022-06-01 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20220601_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilizer',
            old_name='generationId',
            new_name='generation',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='GenerationId',
            new_name='generation',
        ),
    ]