# Generated by Django 4.2.3 on 2023-08-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_about_profile_chessdotcom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='user-icon-image-placeholder.jpg', null=True, upload_to='images'),
        ),
    ]
