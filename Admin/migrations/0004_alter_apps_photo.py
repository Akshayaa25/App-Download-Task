# Generated by Django 4.2.1 on 2023-05-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_apps_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
