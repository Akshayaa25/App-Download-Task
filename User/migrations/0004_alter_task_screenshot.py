# Generated by Django 4.2.1 on 2023-05-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_task_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='Upload/screenshot/'),
        ),
    ]
