# Generated by Django 5.0.6 on 2024-06-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('addess', models.TextField()),
                ('file', models.FileField(upload_to='files/')),
                ('url', models.URLField()),
            ],
        ),
    ]
