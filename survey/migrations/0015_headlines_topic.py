# Generated by Django 3.2.13 on 2022-06-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0014_auto_20220626_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlines',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]