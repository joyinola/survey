# Generated by Django 3.1.1 on 2022-04-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headLine', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prolificId', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=50)),
                ('age', models.CharField(choices=[('Less than 20', 'Less than 20'), ('20-35', '20-35'), ('36-45', '36-45'), ('Above 45', 'Above 45')], max_length=50)),
                ('qualification', models.CharField(choices=[('Less than High School', 'Less than High School'), ('College Degree', 'College Degree'), ('Doctorate Degree', 'Doctorate Degree'), ('PhD holder', 'PhD holder')], max_length=50)),
                ('confirmationCode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UpVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.headlines')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.utilizer')),
            ],
        ),
        migrations.CreateModel(
            name='DownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.headlines')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.utilizer')),
            ],
        ),
    ]
