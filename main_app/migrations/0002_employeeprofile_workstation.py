# Generated by Django 3.1 on 2020-09-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='workstation',
            field=models.CharField(default='Hyderabad', max_length=50),
        ),
    ]