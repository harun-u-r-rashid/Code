# Generated by Django 5.0 on 2024-01-18 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskaddmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='taskaddmodel',
            name='title',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
