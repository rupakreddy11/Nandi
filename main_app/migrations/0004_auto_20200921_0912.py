# Generated by Django 3.1 on 2020-09-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='aadhar_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='customers',
            name='alternate_mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='pan_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customers',
            name='qualification',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='tractor_name_model',
            field=models.CharField(max_length=300),
        ),
    ]