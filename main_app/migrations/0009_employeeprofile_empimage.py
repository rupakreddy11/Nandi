# Generated by Django 3.1 on 2020-09-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200921_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='empimage',
            field=models.ImageField(blank=True, upload_to='Images'),
        ),
    ]
