# Generated by Django 5.1.1 on 2024-09-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjatask',
            name='priority',
        ),
        migrations.AlterField(
            model_name='ninjatask',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
