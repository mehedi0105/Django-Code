# Generated by Django 5.0.6 on 2024-05-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Rahim'),
        ),
    ]