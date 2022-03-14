# Generated by Django 4.0.3 on 2022-03-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='urgency',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
