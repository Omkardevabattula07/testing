# Generated by Django 4.2.11 on 2024-05-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to='profile_pics/'),
            preserve_default=False,
        ),
    ]
