# Generated by Django 5.0 on 2024-01-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0004_taskcompletemodel_delete_completemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskaddmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='taskaddmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TaskCompleteModel',
        ),
    ]